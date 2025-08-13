import os
import sys
from dotenv import load_dotenv
from google.genai import types
from google import genai

from call_function import available_functions

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

def main(): 
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key = api_key)

    verbose = '--verbose' in sys.argv

    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith('--'):
            args.append(arg)

#checks for prompts
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)
        
    user_prompt = " ".join(args)
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

#starts content generation

    response = client.models.generate_content(
            model = 'gemini-2.0-flash-001',
            contents  = messages, 
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt
                                               )
        )

#checks if there are commands    
    if verbose:
        print (f'User prompt: {user_prompt}')
        print (f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print (f'Response tokens: {response.usage_metadata.candidates_token_count}')
    
    if not response.function_calls:
        print (response.text)
    else:
        for function_call_part in response.function_calls: 
            print (f'Calling functions: {function_call_part.name}({function_call_part.args}')
    
    
if __name__ == "__main__":
    main()
