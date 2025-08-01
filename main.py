import os
import sys
from dotenv import load_dotenv
from google.genai import types
from google import genai
from functions.get_files_info import schema_get_files_info

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

def main(): 
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key = api_key)

#checks for prompts
    if len(sys.argv) < 2:
        raise Exception("There is no prompt,exiting with code 1")
        sys.exit(1)

#starts content generation
    response = client.models.generate_content(
            model = 'gemini-2.0-flash-001',
            contents  = sys.argv[1], 
            config=types.GenerateContentConfig(
                tools=[available_functions],system_instruction=system_prompt
                                               )
        )

#checks if there are commands    
    
    if len(sys.argv) < 3:
        print (response.text)

#loops through arguments to find the command
    for arg in sys.argv: 
        if arg == "--verbose":
            print (f'User prompt: {sys.argv[1]}')
            print (f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
            print (f'Response tokens: {response.usage_metadata.candidates_token_count}')
            print (response.text)
    
    
if __name__ == "__main__":
    main()
