import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def main():
	client = OpenAI(
			base_url="https://api.gapgpt.app/v1",
			api_key=os.environ.get("GAPGPT_API_KEY")
	)
      
	response = client.chat.completions.create(
			model="gemini-2.5-flash",
			messages=[{"role": "user", "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."}]
	)
	print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
