import os
import sys
from dotenv import load_dotenv
from google.genai import types
from google import genai

def main(): 
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key = api_key)

    if len(sys.argv) < 2:
        raise Exception("There is no prompt,exiting with code 1")
        sys.exit(1)


    response = client.models.generate_content(
            model = 'gemini-2.0-flash-001',
            contents  = sys.argv[1]
        )
    
    if len(sys.argv) < 3:
        print (response.text)
    for arg in sys.argv: 
        if arg == "--verbose":
            print (f'User prompt: {sys.argv[1]}')
            print (f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
            print (f'Response tokens: {response.usage_metadata.candidates_token_count}')
            print (response.text)
    
    
if __name__ == "__main__":
    main()
