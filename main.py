from operator import contains
import os
import sys
from urllib import response
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info, available_functions

load_dotenv(dotenv_path="key.env")
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
def main():
    if len(sys.argv) < 2:
       print("Error: No prompt provided.")
       sys.exit(1)

    else:
        verbose = "--verbose" in sys.argv
        prompt = [arg for arg in sys.argv[1:] if arg != "--verbose"]
        user_prompt = " ".join(prompt)

    

        response = client.models.generate_content(
            model='gemini-2.0-flash-001', 
            contents=[genai.types.Content(role="user", parts=[{"text": user_prompt}])],
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
                )
            )
        
    
    print("=== Model Response ===")

    # Check if the model made a function call
    function_calls = getattr(response, "function_calls", None)

    if function_calls:
        # Normalize to list if it's a single call
        calls = function_calls if isinstance(function_calls, list) else [function_calls]
        for function_call_part in calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    elif getattr(response, "text", None):
        print(response.text)
    else:
        print("(No function call detected and no text response.)")

    if verbose and hasattr(response, "usage_metadata"):
        usage = response.usage_metadata
        print(f'User prompt: "{user_prompt}"')
        print(f"Prompt tokens: {usage.prompt_token_count}")
        print(f"Response tokens: {usage.candidates_token_count}")



 

if __name__ == "__main__":
   main()
