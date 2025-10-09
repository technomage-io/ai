import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):

    try:
        working_directory_abs = os.path.abspath(working_directory)
        absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
        if os.path.commonpath([absolute_path, working_directory_abs]) != working_directory_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(absolute_path):
            return f'Error: File "{file_path}" not found.'
        if not os.path.splitext(file_path)[1]==".py":
            return f'Error: "{file_path}" is not a Python file.'
        
        
        command = ["python", absolute_path] 
        if args:
            command.extend(args)
        result = subprocess.run(command, capture_output=True, text=True, cwd=working_directory_abs, timeout=30)
      
        
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not output:
            return "No output produced."


        return "\n".join(output) 

    except Exception as e:
             return f"Error: executing Python file: {e}"
    
          

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of command-line arguments to pass to the Python file.",
            ),
        },
    ),
)