import subprocess,os
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a specified python file that is at the specified file, constrained to the working directory, using the given arguments. Then return the output of the python function",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
            "python file": types.Schema(
                type=types.Type.STRING,
                description="The python file that has the python code needed to run these particular programs.",
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    
    #checks the file_path is within the working directory,exists,and is a python file
    abs_working_directory = os.path.abspath(working_directory)
    abs_working_path = os.path.abspath(os.path.join(working_directory,file_path))
    if os.path.isfile(abs_working_path) == False: 
        return f'Error: File "{file_path}" not found.'

    if abs_working_path.startswith(abs_working_directory) == False:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if abs_working_path.endswith(".py") == False:
        return f'Error: "{file_path}" is not a Python file.'
    else: 
        
        
        try:
            commands=['python3', abs_working_path] 
            python_output= subprocess.run(commands + args,
                   cwd=abs_working_directory,
                    timeout=30,
                    capture_output=True, 
                    check=True
            )
            
            HR_output = python_output.stdout.decode('utf-8')
            HR_stderr =python_output.stderr.decode('utf-8')
            if not HR_output and not HR_stderr:
                return 'No output produced'
            else:
                return f'STDOUT:{HR_output} STDERR: {HR_stderr}'
        
        except subprocess.CalledProcessError as e: 
            return f'Process exited with code {e.returncode}'
        except Exception as e: 
            return f"Error: executing Python file: {e}"
