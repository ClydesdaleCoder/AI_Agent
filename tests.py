# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

print ("Result for calculator and lorem")
result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print (result1)

print ("Result for pkg/morlorem file")
result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print (result2)

print ("Result for /tmp/temp.txt file")
result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print (result3)

