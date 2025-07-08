import os


def get_files_info(working_directory, directory=None):
    #get the target here
    if directory == None: 
        target_directory = working_directory
    else:
        target_directory = os.path.join(working_directory, directory)

#confirm we have the correct paths here
    w_absolute = os.path.abspath(working_directory)
    target_absolute = os.path.abspath(target_directory)
    
    if target_absolute.startswith(w_absolute) == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
#make sure we are working with directories

    if os.path.isfile(target_directory) or os.path.isdir(target_directory) == False : 
        return f'Error: "{directory}" is not a directory'  

    # main functionality of this
    else:
        try:
            target_list = os.listdir(target_directory)
            info_list = ''
            for item in target_list:
                file_info = '' 
                item_path = os.path.join(target_directory, item)
                item_size = os.path.getsize(item_path)
                dir_status = os.path.isdir(item_path)    
                file_info = f'- {item}: file_size ={item_size} bytes, is_dir={dir_status}\n'
                info_list = info_list + file_info
        except Exception as e: 
            return f"Error listing files: {e}" 

        return info_list


def get_file_content(working_directory, file_path):
    #checks file_path is a file
    if os.path.isfile(file_path) == False: 
        return f'Error: File not found or is not a regular file: "{file_path}"'

    #checks the file_path is within the working directory
    abs_working_directory = os.path.abspath(working_directory)
    abs_working_path = os.path.abspath(file_path)
    if abs_working_path.startswith(abs_working_directory) == False: 
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    else: 
        try: 


        except Exception as e: 
            return ff"Error getting file information occurred: {e}"
    

