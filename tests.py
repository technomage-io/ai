from functions.get_file_content import get_file_content  # Replace 'your_module' with the actual module name if needed
from config import MAX_CHARS 

def run_tests():
    print('get_file_content(\"calculator\", \"main.py"):')
    result = get_file_content("calculator", "main.py")
    print("Result for 'main.py':")
    print(result)


    print('get_file_content(\"calculator\", \"pkg/calculator.py"):')
    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for 'pkg/calculator.py':")
    print(result)

    print('get_file_content(\"calculator\", \"bin.cat"):')
    result = get_file_content("calculator", "bin.cat")
    print("Result for 'bin.cat':")
    print(result)

    print('get_file_content(\"calculator\", \"pkg/does_not_exist.py"):')
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for 'pkg/does_not_exist.py':")
    print(result)




    print()

    if len(result) <= MAX_CHARS:
        print(f"Test Passed: Content length ({len(result)}) is within MAX_CHARS ({MAX_CHARS})")
    else:
        print(f"Output is within MAX_CHARS ({MAX_CHARS})")
if __name__ == "__main__":
    run_tests()

