import openai

API_KEY = open("OPENAI_API_KEY", "r").read()
openai.api_key = API_KEY

