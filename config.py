from pathlib import Path
import openai
import json
import os

def save(settings_file, settings):
    with open(settings_file, "w") as f:
        json.dump(settings, f, indent=4)

def load(settings_file):
    settings_file = Path(__file__).parent / settings_file
    if os.path.exists(settings_file):
        with open(settings_file, "r") as f:
            settings = json.load(f)
    else:
        settings = {}

    if "assistant_id" not in settings:
        generic_instructions = """You are a fun and helpful AI EdTech assistant helping teenager students to learn effectively.
        You must consider the files provided by the user to provide a response by using the file_search tool
        If the student says something wrong according to the file, or your knowledge, you must correct them
        and provide ways of learning effectively, like memory techniques related to the thing that the student wrongly said
        Consider effective memory techniques, study habits, and learning strategies to help the student learn effectively
        You might also create fun songs or rhymes to help the student remember the information better."""
        user_info = """The user is a teenager student who was born on 2005-01-01 and is studying in the 10th grade.
        He is passionate about Formula 1 and football. His favorite singer is Ed Sheeran and he loves to play the guitar.
        He has a dog named Max and he loves to play with him. Please use this information to make the conversation more engaging
        and to provide personalized learning strategies and memory techniques."""
        print("INFO: Creating an assistant")
        assistant = openai.beta.assistants.create(
            instructions=generic_instructions + user_info,
            model="gpt-3.5-turbo-1106",
            name="EdTech Assistant",
            tools=[
                {"type": "file_search"},
            ]
        )
        settings["assistant_id"] = assistant.id
        save(settings_file, settings)

    return settings