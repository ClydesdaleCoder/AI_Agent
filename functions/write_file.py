import os

def write_file(working_directory, file_path,content):

    #checks the file_path is within the working directory
    abs_working_directory = os.path.abspath(working_directory)
    abs_working_path = os.path.abspath(os.path.join(working_directory,file_path))
    if abs_working_path.startswith(abs_working_directory) == False:
        return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
    
    else:
        try:

            full_file_path = os.path.join(working_directory,file_path)

            with open(full_file_path, "w") as f:
                    
            #checks file_path is a file
                if os.path.exists(full_file_path) == False:
                    os.mkdir(f)

                f.write(content)
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

        except Exception as e:
            return f"Error getting file information occurred: {e}"

