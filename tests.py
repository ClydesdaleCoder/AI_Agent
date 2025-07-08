# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info

print ("Result for current directory")
result1 = get_files_info("calculator", ".")
print (result1)

print ("Result for pkg directory")
result2 = get_files_info("calculator", "pkg")
print (result2)

print ("Result for /bin directory")
result3 = get_files_info("calculator", "/bin")
print (result3)

print ('Result for upper directory') 
result4 = get_files_info("calculator", "../")
print (result4)
