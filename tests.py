# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

print ("Result for main.py")
result1 = get_file_content("calculator", "main.py")
print (result1)

print ("Result for pkg/calculator file")
result2 = get_file_content("calculator", "pkg/calculator.py")
print (result2)

print ("Result for /bin/cat file")
result3 = get_file_content("calculator", "/bin/cat")
print (result3)

