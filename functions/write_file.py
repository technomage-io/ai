import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        abs_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not abs_path.startswith(working_dir_abs + os.sep):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(abs_path):
            try:
                os.makedirs(os.path.dirname(abs_path), exist_ok=True)
            except Exception as e:
                return f"Error: creating directory: {e}"

        if os.path.exists(abs_path) and os.path.isdir(abs_path):
            return f'Error: "{file_path}" is a directory, not a file'

        try:
            with open(abs_path, "w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return f"Error: writing to file: {e}"

    except Exception as e:
        return f"Error: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write into the file.",
            ),
        },
        required=["file_path", "content"]
    ),
)