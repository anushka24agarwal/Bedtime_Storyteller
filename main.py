from dotenv import load_dotenv
load_dotenv() 

from storyteller import generate_story
from judge import judge_story


MAX_REVISIONS = 2

def tell_bedtime_story(user_request: str) -> str:
    story = generate_story(user_request)
    
    for attempt in range(MAX_REVISIONS):
        judgment = judge_story(story)

        if judgment["verdict"] == "APPROVE":
            print(f"Story approved after {attempt + 1} attempt(s).")
            return story

        print(f"Revision needed (attempt {attempt + 1}).")
        story = generate_story(
            user_request=user_request,
            feedback=judgment["feedback"]
        )

    print("Max revisions reached. Returning best version.")
    return story

def is_valid_story_request(user_input: str) -> bool:
    # Must not be empty
    if not user_input.strip():
        return False
    # Must contain at least one alphabet character
    if not any(c.isalpha() for c in user_input):
        return False
    # Optional: reject extremely short inputs
    if len(user_input.strip()) < 3:
        return False
    return True


def main():
    print("\n" + "Welcome to the Bedtime Storyteller!".center(70) + "\n") 

    while True:
        user_request = input(
            "\nWhat kind of bedtime story would you like?\n> "
        ).strip()

        if user_request.lower() == "good night":
            print("\nGood night! Sweet dreams!")
            break

        if not is_valid_story_request(user_request):
            print("\nHmm, that doesn't seem like a story request. Try something like 'A bedtime story about a sleepy bunny'.")
            continue

        final_story = tell_bedtime_story(user_request)

        print("\n" + ">>> BEDTIME STORY <<<".center(70) + "\n")
        print(final_story)

        follow_up = input(
            "\nWould you like another story? (y/n)\n"
            "Or type 'good night' to quit:\n> "
        ).strip().lower()

        if follow_up == "good night" or follow_up == "n":
            print("\nGood night! Sweet dreams!")
            break


if __name__ == "__main__":
    main()