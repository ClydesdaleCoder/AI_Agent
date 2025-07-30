# from subdirectory.filename import function_name
from functions.run_python import run_python_file

print ("Result for calculator and main")
result1 = run_python_file("calculator", "main.py")
print (result1)

print ("Result for calculatore,main , 3+5 file")
result2 = run_python_file("calculator", "main.py", ["3 + 5"])
print (result2)

print ("Result for calculator and main file")
result3 = run_python_file("calculator", "../main.py")
print (result3)

print ("Result for calculator and nonexistent file")
result4 = run_python_file("calculator", "nonexistent.py")
print (result4)