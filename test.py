from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def call_gpt(prompt):
    try:
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
        print(response)
        if "choices" in response:
            return response.choices[0].message.content
        else:
            raise ValueError("Invalid API response format")
    except Exception as e:
        print(f"Error during OpenAI API call: {e}")
        return None

idea_prompt = "Generate a one-sentence story idea."
idea = call_gpt(idea_prompt)
print(idea)

"""
#Agent 2: Story Outliner
outline_prompt = f"Create a 100 word structured outline for a story based on this idea: {idea}. Include the setting, characters, rising action, climax, falling action, and resolution."
story_outline = API_request(outline_prompt)

#Agent 3: Story Writer
story_prompt = f"Generate a 250-750 word story given the following idea and story outline.\
                idea: {idea}\
                story outline: {story_outline}"
written_story = call_gpt(story_prompt)

#Agent 4: Title Generator
title_prompt = f"Create a 1 word title based on this story: {written_story}. Provide only the title."
title = API_request(title_prompt)

#create JSON file for each story
data = {
    "idea" : str(idea),
    "story_outline" : str(story_outline),
    "written_story" : str(written_story)
}

folder_path = "outputs/"
file_name = str(title) + ".json"

file_path = folder_path + file_name

print(file_path)

# Save the JSON data to the file
with open(file_path, "w") as f:
    json.dump(data, f, indent=4) 
"""