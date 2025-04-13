import unittest
from aiflow.lexer import Lexer
from aiflow.parser import Parser, WorkflowNode, StepNode, ConditionNode

class TestParser(unittest.TestCase):
    def test_parse_basic_workflow(self):
        # Test parsing a basic workflow
        code = """
        workflow TestWorkflow {
            input: text;
            
            step Process {
                model: "gpt-3.5-turbo";
                prompt: "Process this text: {{text}}";
                output: result;
            }
            
            return: result;
        }
        """
        
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Check that the AST is a WorkflowNode
        self.assertIsInstance(ast, WorkflowNode)
        
        # Check workflow properties
        self.assertEqual(ast.name, "TestWorkflow")
        self.assertEqual(ast.input_type, "text")
        self.assertEqual(ast.return_var, "result")
        
        # Check that there is one step
        self.assertEqual(len(ast.steps), 1)
        
        # Check step properties
        step = ast.steps[0]
        self.assertIsInstance(step, StepNode)
        self.assertEqual(step.name, "Process")
        self.assertEqual(step.model, "gpt-3.5-turbo")
        self.assertEqual(step.prompt, "Process this text: {{text}}")
        self.assertEqual(step.output, "result")
    
    def test_parse_multiple_steps(self):
        # Test parsing a workflow with multiple steps
        code = """
        workflow MultiStepWorkflow {
            input: text;
            
            step StepOne {
                model: "gpt-4";
                prompt: "First step: {{text}}";
                output: intermediate;
            }
            
            step StepTwo {
                model: "gpt-3.5-turbo";
                prompt: "Second step: {{intermediate}}";
                output: result;
            }
            
            return: result;
        }
        """
        
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Check that there are two steps
        self.assertEqual(len(ast.steps), 2)
        
        # Check first step
        step1 = ast.steps[0]
        self.assertEqual(step1.name, "StepOne")
        self.assertEqual(step1.output, "intermediate")
        
        # Check second step
        step2 = ast.steps[1]
        self.assertEqual(step2.name, "StepTwo")
        self.assertEqual(step2.output, "result")
    
    def test_parse_conditional_workflow(self):
        # Test parsing a workflow with conditional statements
        code = """
        workflow ConditionalWorkflow {
            input: text;
            
            step Analyze {
                model: "gpt-4";
                prompt: "Analyze: {{text}}";
                output: analysis;
            }
            
            if (exists:analysis) {
                step TrueStep {
                    model: "gpt-3.5-turbo";
                    prompt: "True branch: {{analysis}}";
                    output: result;
                }
            } else {
                step FalseStep {
                    model: "gpt-3.5-turbo";
                    prompt: "False branch: {{text}}";
                    output: result;
                }
            }
            
            return: result;
        }
        """
        
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Check that there are two steps (one regular step and one conditional)
        self.assertEqual(len(ast.steps), 2)
        
        # Check that the second step is a ConditionNode
        condition_node = ast.steps[1]
        self.assertIsInstance(condition_node, ConditionNode)
        
        # Check condition properties
        self.assertEqual(condition_node.condition, "exists:analysis")
        
        # Check true branch
        self.assertIsInstance(condition_node.true_step, StepNode)
        self.assertEqual(condition_node.true_step.name, "TrueStep")
        
        # Check false branch
        self.assertIsInstance(condition_node.false_step, StepNode)
        self.assertEqual(condition_node.false_step.name, "FalseStep")
    
    def test_parse_error_handling(self):
        # Test that an exception is raised for invalid syntax
        code = """
        workflow InvalidWorkflow {
            input: text;
            
            step MissingClosingBrace {
                model: "gpt-3.5-turbo";
                prompt: "This step is missing a closing brace";
                output: result;
            
            return: result;
        }
        """
        
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        
        # This should raise an exception due to the missing closing brace
        with self.assertRaises(Exception):
            parser.parse()

if __name__ == '__main__':
    unittest.main()