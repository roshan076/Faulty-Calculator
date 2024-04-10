# Faulty Calculator

This is a simple Python calculator program with intentional faults in certain calculations. The program accepts mathematical operations (+, -, *, /) and returns results that are intentionally incorrect for specific input values.

## How it Works

The program prompts the user to input a mathematical operator (+, -, *, /) and two numbers. It then performs the requested operation but introduces deliberate errors in certain cases. These errors are hardcoded into the program and modify the result to specific incorrect values.

### Examples of Faults

- For input `5.5 + 5`, the program returns `60` instead of the correct answer.
- For input `253 * x`, the program returns `28` instead of the correct answer, where `x` is any number.
- For input `12 / 6`, the program returns `6` instead of the correct answer.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/faulty-calculator.git
