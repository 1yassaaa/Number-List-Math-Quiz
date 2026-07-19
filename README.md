# Number List Math Quiz

A command-line Python quiz game that tests mental math using randomly generated number lists.

## How It Works

1. Choose a difficulty: **Easy**, **Medium**, or **Hard**.
2. Each difficulty sets the number of questions, list size, and number range:

| Difficulty | Questions | List Size | Number Range |
|------------|-----------|-----------|---------------|
| Easy       | 4         | 3         | 5–10          |
| Medium     | 5         | 4         | 5–15          |
| Hard       | 6         | 5         | 10–20         |

3. For each round, a random list of numbers is generated and displayed.
4. You'll be asked one of four question types:
   - **Sum** — total of all numbers in the list
   - **Difference** — max minus min
   - **Count above average** — how many numbers exceed the list's average
   - **Product** — multiply the numbers at two given positions
5. The final question is a **Challenge Question**, using a list with double the usual size.

## Scoring

- Correct answers increase your score.
- After the final question, you'll see:
  - Total time taken
  - Score and percentage
  - Average time per question
  - A "Perfect score!" message if you answer everything correctly.

## Running the Quiz

```bash
python randomMathQuiz.py
```

Follow the on-screen prompts to select a difficulty and answer each question with an integer.

## Requirements

- Python 3.x
- No external dependencies (uses only `random` and `time` from the standard library)

## Author

Yasiru Senavirathna"# Number-List-Math-Quiz" 
