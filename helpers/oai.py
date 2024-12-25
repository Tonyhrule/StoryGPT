from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

# Retrieve the API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)
"""
def API_request(prompt):
    #print("this works")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a creative writer."},
        {
            "role": "user",
            "content": prompt
            }
        ]
    )
    return response.choices[0].message.content
"""
def call_gpt(client, prompt, model="gpt-3.5-turbo"):
    messages=[
        {"role": "system", "content": "You are a creative writer."},
        {
            "role": "user",
            "content": prompt
            }
        ]
    try:
        response = client.chat.completions.create(model=model, messages=messages)
        if "choices" in response and response.choices:
            return response.choices[0].message.content
        else:
            raise ValueError("Invalid API response format")
    except Exception as e:
        print(f"Error during OpenAI API call: {e}")
        return None

test = call_gpt(client, "say hi")
print