from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

# Retrieve the API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

def call_gpt(prompt, client=client, model="gpt-3.5-turbo"):
    messages=[
        {"role": "system", "content": "You are a creative writer."},
        {
            "role": "user",
            "content": prompt
            }
        ]
    try:
        response = client.chat.completions.create(model=model, messages=messages)
        if hasattr(response, "choices") and response.choices:
            return response.choices[0].message.content
        else:
            raise ValueError("Invalid API response format")
    except Exception as e:
        print(f"Error during OpenAI API call: {e}")
        return None