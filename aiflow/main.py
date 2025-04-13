# aiflow/main.py
from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter

def run_workflow(workflow_code, input_data, mock_mode=False):
    """Run a workflow with the given input data.
    
    Args:
        workflow_code (str): The AIFlow code to execute
        input_data (str): The input data for the workflow
        mock_mode (bool): If True, use mock responses instead of calling APIs
    
    Returns:
        str: The result of the workflow execution
    """
    # Tokenize the workflow code
    lexer = Lexer(workflow_code)
    tokens = lexer.tokenize()
    
    # Parse the tokens into an AST
    parser = Parser(tokens)
    ast = parser.parse()
    
    # Execute the workflow
    interpreter = Interpreter(ast, mock_mode=mock_mode)
    result = interpreter.execute(input_data)
    
    return result

def main():
    # Example workflow
    workflow_code = """
    workflow TextProcessor {
        input: text;
        
        step Summarize {
            model: "gpt-3.5-turbo";
            prompt: "Summarize the following text: {{text}}";
            output: summary;
        }
        
        step Elaborate {
            model: "gpt-3.5-turbo";
            prompt: "Elaborate on this summary with more details: {{summary}}";
            output: response;
        }
        
        return: response;
    }
    """
    
    # Example input
    input_text = "Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to natural intelligence displayed by animals including humans. AI research has been defined as the field of study of intelligent agents, which refers to any system that perceives its environment and takes actions that maximize its chance of achieving its goals."
    
    # Run the workflow in mock mode
    result = run_workflow(workflow_code, input_text, mock_mode=True)
    print(result)

if __name__ == "__main__":
    main()