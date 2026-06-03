import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def main():
		client = OpenAI(
			base_url="https://openrouter.ai/api/v1",
			api_key=os.environ.get("OPENROUTER_NYX_CODE_KEY")
		)
		
		model = "openrouter/owl-alpha"
					
		response = client.chat.completions.create(
			model=model,
			messages=[{"role": "user", "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."}]
		)
		print('Prompt Tokens:', response.usage.prompt_tokens)
		print('Completion Tokens:', response.usage.completion_tokens)
		print('Total Tokens:', response.usage.total_tokens)
		print('Response:', response.choices[0].message.content)


if __name__ == "__main__":
	main()
