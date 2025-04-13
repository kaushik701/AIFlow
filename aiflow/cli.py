import argparse
import sys
import os
from pathlib import Path
from dotenv import load_dotenv
from .main import run_workflow

def check_env_file():
    """Check if .env file exists and contains required API keys."""
    # Try to load from current directory first
    env_path = Path('.env')
    if not env_path.exists():
        # Try to load from project root directory
        project_root = Path(__file__).parent.parent
        env_path = project_root / '.env'
    
    if not env_path.exists():
        print("Warning: No .env file found. You'll need to set up your API keys.")
        print("Create a .env file with the following content:")
        print("OPENAI_API_KEY=your_openai_api_key_here")
        print("\nOr set these environment variables manually.")
        
        # Check if API keys are set in environment
        if not os.environ.get("OPENAI_API_KEY"):
            print("\nNo OPENAI_API_KEY found in environment variables.")
            print("AIFlow requires API keys to function properly.")
            print("You can use --mock mode to test without API keys.")
            choice = input("Do you want to continue anyway? (y/n): ")
            if choice.lower() != 'y':
                sys.exit(1)
    else:
        # Load the .env file
        load_dotenv(env_path)
        
        # Check if required keys are in the loaded .env
        if not os.environ.get("OPENAI_API_KEY"):
            print("Warning: OPENAI_API_KEY not found in .env file.")
            print("Please add your OpenAI API key to the .env file.")
            print("You can use --mock mode to test without API keys.")
            choice = input("Do you want to continue anyway? (y/n): ")
            if choice.lower() != 'y':
                sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='AIFlow - A language for AI workflows')
    parser.add_argument('file', help='AIFlow file to execute')
    parser.add_argument('--input', help='Input data for the workflow')
    parser.add_argument('--input-file', help='File containing input data for the workflow')
    parser.add_argument('--mock', action='store_true', help='Run in mock mode without making API calls')
    
    args = parser.parse_args()
    
    # Only check for API keys if not in mock mode
    if not args.mock:
        check_env_file()
    
    # Read the workflow code
    with open(args.file, 'r') as f:
        workflow_code = f.read()
    
    # Get the input data
    if args.input:
        input_data = args.input
    elif args.input_file:
        with open(args.input_file, 'r') as f:
            input_data = f.read()
    else:
        print("Reading input from stdin. Press Ctrl+D (Unix) or Ctrl+Z (Windows) followed by Enter to end input.")
        input_data = sys.stdin.read()
    
    # Run the workflow
    result = run_workflow(workflow_code, input_data, mock_mode=args.mock)
    print(result)

if __name__ == "__main__":
    main()