import os
import sys
from dotenv import load_dotenv
from google.genai import types
from google import genai

from call_function import available_functions, function_map

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
    generate_content(client,messages,verbose)

#starts content generation
def generate_content(client,messages,verbose):
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
        print (f'User prompt: {messages}')
        print (f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print (f'Response tokens: {response.usage_metadata.candidates_token_count}')
    
    if not response.function_calls:
        print (response.text)
    else:
        for function_call_part in response.function_calls: 
            function_call_result = call_function(function_call_part,verbose)
            if not function_call_result.parts[0].function_response.response:
                raise Exception ( 'Function called did not return proper response')
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

            

                    
                
                    
def call_function(function_call_part, verbose=False):
    if verbose: 
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    if function_call_part.name in function_map:
        args = function_call_part.args
        args['working_directory'] = './calculator'
        called_function = function_map[function_call_part.name]
        result = called_function(**args)
        return types.Content(
            role="tool",
            parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result },
            )
        ],
    )
        
    else: 
        return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"error": f"Unknown function: {function_call_part.name}"},
            )
        ],
    )
         
if __name__ == "__main__":
    main()
