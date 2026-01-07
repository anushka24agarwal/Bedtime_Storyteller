from openai import OpenAI
from prompts import STORYTELLER_SYSTEM_PROMPT, storyteller_user_prompt

client = OpenAI()

MODEL_NAME = "gpt-3.5-turbo"  # example — use the model provided in the skeleton

def generate_story(user_request: str, feedback: str | None = None) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": STORYTELLER_SYSTEM_PROMPT},
            {"role": "user", "content": storyteller_user_prompt(user_request, feedback)},
        ],
        temperature=0.8,
    )

    return response.choices[0].message.content.strip()
