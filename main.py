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
    max_iterations = 20
    for step in range(max_iterations):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt
        ),
    )
            if verbose and hasattr(response, "usage_metadata"):
                print(f"\nStep {step + 1}")
                print("Prompt tokens:", response.usage_metadata.prompt_token_count)
                print("Response tokens:", response.usage_metadata.candidates_token_count)

            for candidate in response.candidates:
                messages.append(candidate.content)

            if response.text:
               print(response.text)
               break
            
            
            all_results = []

            for function_call_part in response.function_calls:
                function_call_result = call_function(function_call_part, verbose=verbose)

                try:
                    result_payload = function_call_result.parts[0].function_response.response
                except Exception:
                    raise RuntimeError("Fatal: Function response missing or malformed.")
       
                print(result_payload["result"])

                messages.append(
                    types.Content(
                        role="user",
                        parts=[types.Part.from_function_response(
                            name=function_call_part.name,
                            response=result_payload
                        )]
                    )
                )

        except Exception as e:
            print(f"Error during step {step + 1}: {e}")
            break




if __name__ == "__main__":
    main()
