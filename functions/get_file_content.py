import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
 

    try:
        working_directory_abs = os.path.abspath(working_directory)
        absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
        if os.path.commonpath([absolute_path, working_directory_abs]) != working_directory_abs:
            return f'Error: Cannot Access "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(absolute_path):
            return f'Error: "{file_path}" is not a file'

        
        with open(absolute_path, 'r') as file:
            content = file.read(MAX_CHARS)

        return content

    except Exception as e:
        return f'Error: {str(e)}'