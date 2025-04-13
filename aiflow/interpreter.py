import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Interpreter:
    def __init__(self, ast, mock_mode=False):
        self.ast = ast
        self.variables = {}
        self.mock_mode = mock_mode
        
        # Initialize API clients if not in mock mode
        if not mock_mode:
            self.openai_client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        
    def execute(self, input_data):
        """Execute the workflow with the given input data."""
        # Store the input in variables
        self.variables = {self.ast.input_type: input_data}
        
        # Execute each step
        for step in self.ast.steps:
            if hasattr(step, 'condition'):  # This is a ConditionNode
                self.execute_condition(step)
            else:  # This is a regular StepNode
                self.execute_step(step)
            
        # Return the final output
        return self.variables[self.ast.return_var]
    
    def execute_step(self, step):
        """Execute a single step in the workflow."""
        # Process the prompt template
        prompt = step.prompt
        for var_name in self.variables:
            template_var = f"{{{{{var_name}}}}}"
            if template_var in prompt:
                prompt = prompt.replace(template_var, str(self.variables[var_name]))
            
        # Call the appropriate AI model or use mock response
        if self.mock_mode:
            response = self._get_mock_response(step.name, prompt)
        elif "gpt" in step.model:
            response = self.call_openai(step.model, prompt)
        else:
            raise Exception(f"Unsupported model: {step.model}")
            
        # Store the output
        self.variables[step.output] = response
    
    def execute_condition(self, condition_node):
        """Execute a conditional step in the workflow."""
        # Evaluate the condition
        condition_result = self.evaluate_condition(condition_node.condition)
        
        if condition_result:
            self.execute_step(condition_node.true_step)
        elif condition_node.false_step:
            self.execute_step(condition_node.false_step)
    
    def evaluate_condition(self, condition):
        """Evaluate a condition expression."""
        # For now, we'll implement a simple condition evaluator
        # that checks if a variable exists and is truthy
        if condition.startswith('exists:'):
            var_name = condition[7:].strip()
            return var_name in self.variables and bool(self.variables[var_name])
        
        # Add more condition types as needed
        return False
    
    def _get_mock_response(self, step_name, prompt):
        """Generate a mock response for testing without API calls."""
        if "Sentiment" in step_name:
            return "positive"
        elif "Positive" in step_name:
            return "Thank you for your positive feedback! We're thrilled to hear that our product has made your life easier. Your satisfaction is our top priority, and we're committed to continuing to provide you with excellent service."
        elif "Negative" in step_name:
            return "We appreciate your feedback and are sorry to hear about your concerns. We take all feedback seriously and would like to address your issues. Please let us know how we can improve your experience."
        else:
            return f"Mock response for {step_name}: {prompt[:30]}..."
        
    def call_openai(self, model, prompt):
        """Call an OpenAI model using the new API format."""
        response = self.openai_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content