import unittest
from aiflow.lexer import Lexer, Token

class TestLexer(unittest.TestCase):
    def test_tokenize_basic_workflow(self):
        # Test a basic workflow
        code = """
        workflow TestWorkflow {
            input: text;
            
            step Process {
                model: "gpt-4";
                prompt: "Process this text: {{text}}";
                output: result;
            }
            
            return: result;
        }
        """
        
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        # Check that the correct number of tokens were generated
        self.assertGreater(len(tokens), 0)
        
        # Check that the first token is the workflow keyword
        self.assertEqual(tokens[0].type, 'KEYWORD')
        self.assertEqual(tokens[0].value, 'workflow')
        
        # Check that the identifier token is next
        self.assertEqual(tokens[1].type, 'IDENTIFIER')
        self.assertEqual(tokens[1].value, 'TestWorkflow')
        
        # Check for opening brace
        self.assertEqual(tokens[2].type, 'SPECIAL')
        self.assertEqual(tokens[2].value, '{')
    
    def test_tokenize_with_template_vars(self):
        # Test that strings with template variables are properly tokenized as strings
        code = """
        workflow Test {
            input: text;
            step Process {
                model: "gpt-3.5-turbo";
                prompt: "Process {{text}}";
                output: result;
            }
            return: result;
        }
        """
        
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        # Find the string token that contains the template variable
        prompt_string = None
        for i, token in enumerate(tokens):
            if token.type == 'STRING' and '{{text}}' in token.value:
                prompt_string = token
                break
        
        # Verify that the string with the template variable was tokenized correctly
        self.assertIsNotNone(prompt_string, "String with template variable not found")
        self.assertEqual(prompt_string.value, "Process {{text}}")
    
    def test_tokenize_conditional_workflow(self):
        # Test a workflow with conditional statements
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
                    model: "gpt-4";
                    prompt: "True branch: {{analysis}}";
                    output: result;
                }
            } else {
                step FalseStep {
                    model: "gpt-4";
                    prompt: "False branch: {{text}}";
                    output: result;
                }
            }
            
            return: result;
        }
        """
        
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        # Check for the if keyword
        if_token = None
        for token in tokens:
            if token.type == 'KEYWORD' and token.value == 'if':
                if_token = token
                break
        
        self.assertIsNotNone(if_token)
        
        # Check for the else keyword
        else_token = None
        for token in tokens:
            if token.type == 'KEYWORD' and token.value == 'else':
                else_token = token
                break
        
        self.assertIsNotNone(else_token)
    
    def test_invalid_character(self):
        # Test that an exception is raised for invalid characters
        code = "workflow Test { input: text; step Process { model: @invalid; } }"
        
        lexer = Lexer(code)
        with self.assertRaises(Exception) as context:
            lexer.tokenize()
        
        self.assertTrue("Invalid character" in str(context.exception))

if __name__ == '__main__':
    unittest.main()