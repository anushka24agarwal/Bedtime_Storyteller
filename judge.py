from openai import OpenAI
from prompts import JUDGE_SYSTEM_PROMPT, judge_user_prompt

client = OpenAI()

MODEL_NAME = "gpt-3.5-turbo"  # same model, different role

def judge_story(story_text: str) -> dict:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": JUDGE_SYSTEM_PROMPT},
            {"role": "user", "content": judge_user_prompt(story_text)},
        ],
        temperature=0.2,
    )

    content = response.choices[0].message.content.strip()

    verdict = "REVISE"
    if "APPROVE" in content.upper():
        verdict = "APPROVE"

    return {
        "verdict": verdict,
        "feedback": content,
    }
