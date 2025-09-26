from functions.run_python_file import run_python_file  


def run_tests():
   result1 = run_python_file("calculator", "main.py")
   print(result1)
   print()

   result2= run_python_file("calculator", "main.py", ["3 + 5"])
   print(result2)
   print()

   result3 = run_python_file("calculator", "tests.py")
   print(result3)
   print()

   result4 = run_python_file("calculator", "../main.py")
   print(result4)
   print()
    
   result5 = run_python_file("calculator", "nonexistent.py")
   print(result5)
   print()
if __name__ == "__main__":
    run_tests()

