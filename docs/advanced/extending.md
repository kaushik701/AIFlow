# Extending AIFlow

This page provides guidance on how to extend AIFlow with custom functionality.

## Architecture Overview

AIFlow is designed with a modular architecture that allows for extension:

1. **Lexer**: Tokenizes the AIFlow code
2. **Parser**: Parses tokens into an abstract syntax tree (AST)
3. **Interpreter**: Executes the AST
4. **Model Providers**: Interface with AI models (currently OpenAI)

## Adding Custom Model Providers

### Model Provider Interface

To add support for a new AI model provider, you can implement a custom model provider class:

```python
class CustomModelProvider:
    def __init__(self, api_key=None):
        self.api_key = api_key
        # Initialize any other necessary components
    
    def generate_response(self, prompt, model, max_tokens=1000, temperature=0.7):
        """
        Generate a response from the model.
        
        Args:
            prompt (str): The prompt to send to the model
            model (str): The model to use
            max_tokens (int): Maximum number of tokens in the response
            temperature (float): Controls randomness (0.0 to 1.0)
            
        Returns:
            str: The model's response
        """
        # Implement the logic to call your custom model API
        # Return the response text
        pass
```

### Registering a Custom Model Provider

Once you've implemented your custom model provider, you can register it with AIFlow:

```python
from aiflow.interpreter import Interpreter
from custom_provider import CustomModelProvider

# Create an instance of your custom provider
custom_provider = CustomModelProvider(api_key="your_api_key")

# Create an interpreter with your custom provider
interpreter = Interpreter(model_provider=custom_provider)

# Use the interpreter as usual
result = interpreter.interpret(workflow_ast, input_value)
```

## Adding Custom Functions

### Function Decorator

You can extend AIFlow with custom functions using a decorator pattern:

```python
from aiflow.functions import register_function

@register_function
def custom_function(args):
    """
    A custom function that can be used in AIFlow workflows.
    
    Args:
        args: Arguments passed to the function
        
    Returns:
        The result of the function
    """
    # Implement your custom function logic
    return result
```

### Using Custom Functions

Once registered, your custom function can be used in AIFlow workflows:

```
workflow CustomWorkflow {
    input: text;
    
    step ProcessWithCustomFunction {
        model: "gpt-3.5-turbo";
        prompt: "Process this with custom function: {{custom_function(text)}}";
        output: result;
    }
    
    return: result;
}
```

## Custom Output Processors

### Output Processor Interface

You can create custom output processors to transform model outputs:

```python
class CustomOutputProcessor:
    def process(self, output, context=None):
        """
        Process the model output.
        
        Args:
            output (str): The raw output from the model
            context (dict): Additional context information
            
        Returns:
            The processed output
        """
        # Implement your custom processing logic
        return processed_output
```

### Using Custom Output Processors

Register and use your custom output processor:

```python
from aiflow.interpreter import Interpreter
from custom_processor import CustomOutputProcessor

# Create an instance of your custom processor
custom_processor = CustomOutputProcessor()

# Create an interpreter with your custom processor
interpreter = Interpreter(output_processor=custom_processor)

# Use the interpreter as usual
result = interpreter.interpret(workflow_ast, input_value)
```

## Adding Custom Conditions

### Condition Interface

You can implement custom conditions for use in conditional statements:

```python
from aiflow.conditions import register_condition

@register_condition
def custom_condition(variable, value=None):
    """
    A custom condition that can be used in AIFlow workflows.
    
    Args:
        variable: The variable to check
        value: Optional value to compare against
        
    Returns:
        bool: Whether the condition is met
    """
    # Implement your custom condition logic
    return result
```

### Using Custom Conditions

Once registered, your custom condition can be used in AIFlow workflows:

```
workflow CustomConditionWorkflow {
    input: text;
    
    step Process {
        model: "gpt-3.5-turbo";
        prompt: "Process this text: {{text}}";
        output: result;
    }
    
    if (custom_condition:result) {
        step FollowUp {
            model: "gpt-3.5-turbo";
            prompt: "Follow up on this result: {{result}}";
            output: final_result;
        }
    }
    
    return: final_result;
}
```

## Creating Custom CLI Commands

### Command Registration

You can add custom commands to the AIFlow CLI:

```python
from aiflow.cli import register_command

@register_command("custom-command")
def custom_command(args):
    """
    A custom command for the AIFlow CLI.
    
    Args:
        args: Command-line arguments
    """
    # Implement your custom command logic
    pass
```

### Using Custom Commands

Once registered, your custom command can be used from the command line:

```bash
aiflow custom-command [arguments]
```

## Plugin System

### Creating a Plugin

You can create plugins to extend AIFlow with multiple features:

```python
from aiflow.plugins import AIFlowPlugin

class CustomPlugin(AIFlowPlugin):
    def __init__(self):
        super().__init__(name="custom-plugin", version="1.0.0")
    
    def initialize(self):
        """Initialize the plugin."""
        # Register custom components
        self.register_model_provider(CustomModelProvider)
        self.register_function(custom_function)
        self.register_condition(custom_condition)
        self.register_command(custom_command)
    
    def cleanup(self):
        """Clean up resources when the plugin is unloaded."""
        pass
```

### Registering a Plugin

Register your plugin with AIFlow:

```python
from aiflow.plugins import register_plugin
from custom_plugin import CustomPlugin

register_plugin(CustomPlugin())
```

## Best Practices

When extending AIFlow:

1. **Follow the existing patterns**: Maintain consistency with the core codebase
2. **Write tests**: Ensure your extensions work correctly
3. **Document your extensions**: Provide clear documentation for users
4. **Handle errors gracefully**: Implement proper error handling
5. **Consider performance**: Optimize your extensions for performance
6. **Maintain compatibility**: Ensure your extensions work with future AIFlow versions

## Next Steps

- Learn about [contributing to AIFlow](../contributing/contributing.md)
- Understand [security best practices](security.md)
- Explore [performance optimization](performance.md)
