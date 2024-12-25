from openai import OpenAI
import json
client = OpenAI()

#Agent 1: Idea generator
response1 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a creative writer."},
        {
            "role": "user",
            "content": "Generate a one-sentence story idea."
        }
    ]
)

idea = response1.choices[0].message.content

#Agent 2: Story Outliner
response2 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a creative writer."},
        {
            "role": "user",
            "content": f"Create a 100 word structured outline for a story based on this idea: {idea}.\
                Include the setting, characters, rising action, climax, falling action, and resolution."
        }
    ]
)

story_outline = response2.choices[0].message.content

#Agent 3: Story Writer
response3 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a creative writer."},
        {
            "role": "user",
            "content": f"Generate a 250-750 word story given the following idea and story outline.\
                idea: {idea}\
                story outline: {story_outline}"
        }
    ]
)

written_story = response3.choices[0].message.content

#Agent 4: Title generator
response4 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a creative writer."},
        {
            "role": "user",
            "content": f"Create a 1 word title based on this story: {written_story}.\
                provide only the title."
        }
    ]
)

title = response4.choices[0].message.content

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
