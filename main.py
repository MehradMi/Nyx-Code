import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

GAPGPT_BASE_URL = "https://api.gapgpt.app/v1"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

def main():
		parser = argparse.ArgumentParser(description="Chatbot")
		parser.add_argument("user_prompt", type=str, help="User prompt")
		parser.add_argument("--verbose", action="store_true", help="Enable verbose output mode")
		args = parser.parse_args()

		client = OpenAI(
			base_url=GAPGPT_BASE_URL,
			api_key=os.environ.get("GAPGPT_API_KEY")
		)	
		model = "gpt-4.1-nano"

		messages = [{"role": "user", "content": args.user_prompt}]
					
		response = client.chat.completions.create(
			model=model,
			messages=messages
		)
		if args.verbose:
			print('User Prompt:', args.user_prompt)	
			print('Prompt Tokens:', response.usage.prompt_tokens)
			print('Completion Tokens:', response.usage.completion_tokens)
			print('Total Tokens:', response.usage.total_tokens)
		print('Response:', response.choices[0].message.content)


if __name__ == "__main__":
	main()
