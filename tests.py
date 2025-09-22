from functions.get_files_info import get_files_info  # Replace 'your_module' with the actual module name if needed

def run_tests():
    print("get_files_info(\"calculator\", \".\"):")
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)

    print()

    print("get_files_info(\"calculator\", \"pkg\"):")
    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)
    print()

    print("get_files_info(\"calculator\", \"/bin\"):")
    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)
    print()

    print("get_files_info(\"calculator\", \"../\"):")
    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)
    print()

if __name__ == "__main__":
    run_tests()

