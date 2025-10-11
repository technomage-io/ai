import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv(dotenv_path="key.env")
from prompts import system_prompt
from call_function import available_functions
from call_function import call_function

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if verbose and hasattr(response, "usage_metadata"):
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if not response.function_calls:
        print(response.text)
        return
    
    all_results = []

    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose=verbose)

        try:
            result_payload = function_call_result.parts[0].function_response.response
        except Exception:
            raise RuntimeError("Fatal: Function response missing or malformed.")
       
        

        if verbose:
            print(f"-> {result_payload}")
        all_results.append(result_payload)



    print(result_payload["result"])


if __name__ == "__main__":
    main()
