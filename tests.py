from functions.write_file import write_file  


def run_tests():
   result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
   print(result1)
   print()

   result2= write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
   print(result2)
   print()

   result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
   print(result3)
   print()

    
if __name__ == "__main__":
    run_tests()

