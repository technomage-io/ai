from operator import contains
import os
import sys
from dotenv import load_dotenv
from google import genai
load_dotenv(dotenv_path="key.env")
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)

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
            contents=prompt
        )
       


        print("=== Model Response ===")
        print(response.text)

        if verbose:

            usage = response.usage_metadata
            print(f'User prompt: "{user_prompt}"')
            print(f"Prompt tokens: {usage.prompt_token_count}")
            print(f"Response tokens: {usage.candidates_token_count}")


if __name__ == "__main__":
   main()
