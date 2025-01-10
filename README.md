## Overview
Welcome to Story GPT, an application designed to generate endless stories with just a click of a button! Our system builds on a simple multi-agent pipeline that leverages the OpenAI API to expertly craft engaging fictional narratives from scratch. These AI agents work collaboratively to generate short stories while maintaining a transparent overview of the story-creation process, providing both the story idea and initial description in addition to the narrative itself. 
## System Requirements
* Python 3.13 or higher
## Main Components

1. Idea Generator Agent: Generates a one-sentence story idea.
2. Story Outliner Agent: Creates a structured outline based on the idea.
3. Story Writier Agent: Generates a 250-750 word story given the idea and outline.
4. Title Generator Agent: Produces a 1-word title for the story.
5. Saved Stories: Each story is saved in an individual JSON file under the outputs folder
## Getting Started
1. Clone this repository:
   ```
   git clone https://github.com/Tonyhrule/story-gpt.git
   cd story-gpt
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up environment variables: Create a .env file and add your OpenAI API Key
   ```
   OPENAI_API_KEY = "your_api_key_here"
   ```
## Project Structure
```
story-gpt/
│
├── README.md                  # Project overview and setup instructions
├── requirements.txt           # Python dependencies
├── main.py                    # Main script for the multi-agent story-writing pipeline
├── .gitignore                 # Ignore files that should be hidden (e.g. .env)
│
├── helpers/                   # Folder for helper functions
│   └── oai.py                 # Includes function for making API request
│
└── outputs/                   # Folder to save generated stories
    └── output_story.json      # Each generated story will be saved in a file like this with the title as the file name
```
## Customization
You can customize the length of the stories or change the genre and style through editing each agent prompt in main.py
