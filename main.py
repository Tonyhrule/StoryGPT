from openai import OpenAI
client = OpenAI()

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

idea = response1.choices[0].message
#print(idea)

response2 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a creative writer."},
        {
            "role": "user",
            "content": f"Create a 100-word structured outline for a story based on this idea: {idea}\
                include the setting, characters, rising action, climax, falling action, and resolution."
        }
    ]
)

story_outline = response2.choices[0].message
#print(story_outline)

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

written_story = response3.choices[0].message
print(written_story)