import os
from functions.config import MAX_CHARS
from google.genai import types

schema_get_files_content= types.FunctionDeclaration(
    name="get_files_content",
    description="Read and list the content of the specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):

    #checks the file_path is within the working directory
    abs_working_directory = os.path.abspath(working_directory)
    abs_working_path = os.path.abspath(os.path.join(working_directory,file_path))
    if abs_working_path.startswith(abs_working_directory) == False:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    #checks file_path is a file
    full_file_path = os.path.join(working_directory,file_path)
    if os.path.isfile(full_file_path) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'

    else:
        try:

            with open(full_file_path, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                next_char = f.read(1)

                if next_char:
                    return f'{file_content_string}' + '[...File "{full_file_path}" truncated at 10000 characters]'
                else: 
                    return f'{file_content_string}'
                    
        except Exception as e:
            return f"Error getting file information occurred: {e}"
    
