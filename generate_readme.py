import os
import openai
from dotenv import load_dotenv

def generate_readme(api_key, repo_content):
    openai.api_key = api_key

    formatted_prompt = (
        "Create a professional and detailed README.md for a GitHub repository. "
        "The README should be in the correct markdown format, including a Table of Contents, Introduction, Installation, Usage, Features, Contributing, License, and Contact sections. "
        "The content should reflect the following repository data:\n\n"
        f"{repo_content}\n\n"
        "Make sure the README is clear for developers and users to understand and well-formatted."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional assistant skilled at generating README files from GitHub repository content."},
            {"role": "user", "content": formatted_prompt}
        ]
    )

    return response.choices[0].message['content'].strip()
