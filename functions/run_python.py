import subprocess

def run_python_file(working_directory, file_path, args=[]):
    
    #checks the file_path is within the working directory,exists,and is a python file
    abs_working_directory = os.path.abspath(working_directory)
    abs_working_path = os.path.abspath(os.path.join(working_directory,file_path))
    if abs_working_path.exists == False: 
        return f'Error: File "{file_path}" not found.'

    if abs_working_path.startswith(abs_working_directory) == False:
        return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'

    if abs_working_path.endswith(".py") == False:
        return f'Error: "{file_path}" is not a Python file.'
    else: 
        try:
            subprocess.run(
                    file_path,
                    args = args,
                    timeout=30,
                    
            )
        except Exception as e: 
            f"Error: executing Python file: {e}"
