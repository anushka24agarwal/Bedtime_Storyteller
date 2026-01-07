# Bedtime Storyteller 

A Python-based interactive bedtime story generator for children aged 5–10, featuring a storyteller LLM and a judge LLM to ensure age-appropriate, engaging and educational stories.

## Features

- Generates bedtime stories with a clear beginning, middle, and happy ending.
- Adds a short title at the top of every story.
- Includes 3 new vocabulary words with meanings for educational value.
- Judge LLM evaluates the story for age-appropriateness, clarity, engagement, and bedtime suitability.
- Automatic revision loop: if the story is not approved, the storyteller revises it using judge feedback.
- Interactive CLI: ask for multiple stories in a single session.
- Input validation: detects invalid or “garbage” requests and prompts the user to try again.
- Friendly exit: type `good night` to quit the program.

## File Structure 

main.py            # Main interactive CLI loop
storyteller.py     # Handles story generation with the LLM
judge.py           # Evaluates story quality and suggests revisions
prompts.py         # All system and user prompt templates
requirements.txt   # Project dependencies
architecture.png   # Block diagram of system flow
.env               # Your OpenAI API key (not included in repo)

## Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd <repo-folder>
```

2. Create and activate a virtual environment
```bash
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Add your OpenAI API key to a .env file in the project root

## Usage
Run the interactive story generator:
```bash
python main.py
```

- Enter your story request, e.g., A bedtime story about a friendly dragon.
- The program will generate a story with a title and vocabulary section.
- After the story, you will be asked if you want another story or type "good night" to quit.
- Invalid inputs (e.g. random characters) are rejected with a friendly prompt.
