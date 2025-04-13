# tests/test_interpreter.py
import unittest
import os
from unittest.mock import patch, MagicMock
from aiflow.lexer import Lexer
from aiflow.parser import Parser
from aiflow.interpreter import Interpreter

class TestInterpreter(unittest.TestCase):
    def setUp(self):
        # Sample workflow for testing
        self.workflow_code = """
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
        
        # Parse the workflow
        lexer = Lexer(self.workflow_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        self.ast = parser.parse()
        
        # Mock environment variables
        os.environ["OPENAI_API_KEY"] = "test_api_key"
    
    @patch('openai.OpenAI')
    def test_interpreter_initialization(self, mock_openai):
        # Test that the interpreter initializes correctly
        interpreter = Interpreter(self.ast)
        
        # Check that OpenAI client was initialized with the correct API key
        mock_openai.assert_called_once_with(api_key="test_api_key")
        
        # Check that the interpreter has the correct properties
        self.assertEqual(interpreter.ast, self.ast)
        self.assertEqual(interpreter.variables, {})
        self.assertEqual(interpreter.mock_mode, False)
    
    @patch('openai.OpenAI')
    def test_execute_workflow(self, mock_openai):
        # Mock the OpenAI client and its methods
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        # Mock the chat completions create method
        mock_completion = MagicMock()
        mock_client.chat.completions.create.return_value = mock_completion
        
        # Mock the response from OpenAI
        mock_choice = MagicMock()
        mock_choice.message.content = "Processed result"
        mock_completion.choices = [mock_choice]
        
        # Create the interpreter and execute the workflow
        interpreter = Interpreter(self.ast)
        result = interpreter.execute("Test input")
        
        # Check that the OpenAI API was called with the correct parameters
        mock_client.chat.completions.create.assert_called_once()
        call_args = mock_client.chat.completions.create.call_args[1]
        
        self.assertEqual(call_args["model"], "gpt-3.5-turbo")
        self.assertEqual(call_args["messages"][0]["content"], "Process this text: Test input")
        
        # Check that the result is correct
        self.assertEqual(result, "Processed result")
    
    def test_mock_mode(self):
        # Test the interpreter in mock mode
        interpreter = Interpreter(self.ast, mock_mode=True)
        
        # Execute the workflow in mock mode
        result = interpreter.execute("Test input")
        
        # Check that the result contains the expected mock response
        self.assertIn("Mock response for Process", result)
    
    def test_conditional_workflow(self):
        # Create a workflow with conditional logic
        workflow_code = """
        workflow ConditionalTest {
            input: text;
            
            step Analyze {
                model: "gpt-3.5-turbo";
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
        
        # Parse the workflow
        lexer = Lexer(workflow_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Create the interpreter in mock mode
        interpreter = Interpreter(ast, mock_mode=True)
        
        # Execute the workflow
        result = interpreter.execute("Test input")
        
        # The condition should evaluate to True and the TrueStep should be executed
        self.assertIn("True branch", result)
    
    @patch('openai.OpenAI')
    def test_api_error_handling(self, mock_openai):
        # Mock the OpenAI client to raise an exception
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_client.chat.completions.create.side_effect = Exception("API Error")
        
        # Create the interpreter
        interpreter = Interpreter(self.ast)
        
        # Check that the error is properly propagated
        with self.assertRaises(Exception) as context:
            interpreter.execute("Test input")
        
        self.assertTrue("API Error" in str(context.exception))

if __name__ == '__main__':
    unittest.main()