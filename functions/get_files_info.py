import os
import types 
from google.genai import types


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)


def get_files_info(working_directory, directory="."):
   try: 
    working_directory_abs = os.path.abspath(working_directory)
    absolute_path = os.path.abspath(os.path.join(working_directory, directory))
    if os.path.commonpath([absolute_path, working_directory_abs]) != working_directory_abs:
        return f'Error: Cannot List "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(absolute_path):
        return f'Error: "{directory}" is not a directory'



    lines = []
    for entry in os.listdir(absolute_path):
        entry_path = os.path.join(absolute_path, entry)
        is_dir = os.path.isdir(entry_path)
        file_size = os.path.getsize(entry_path)
        lines.append(f'- {entry}: file_size={file_size} bytes, is_dir={is_dir}')

    return "\n".join(lines)

   except Exception as e:
    return f'Error: {str(e)}'

