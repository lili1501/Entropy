```
ENTROPY/
│
├── main.py              # Main game logic + play() function
├── functions.py         # all functions used in main.py/ calc_entropy.py
├── calc_entropy.py.     # keeps all entropy, MI calculation function
├── valid_words.txt      # Dictionary of 5-letter English words (~14.8k words)
└──README.md             # Documentation file (this file)
```

Overview

This project implements a Wordle-style guessing game (used as a valid alternative to Bulls and Cows) enhanced with information theory.
The goal is to show how entropy can guide optimal guessing strategies in deductive search games.

The game:

Lets the user play interactively in the terminal
Computes entropy after every guess
Uses mutual information to suggest the best next guess
Includes an intelligent hint system
Tracks the reduction of uncertainty across rounds

This satisfies:

✔ Part 1: Interactive game + entropy calculations \
✔ Part 2: Strategy based on entropy and mutual information

🎮 Game Description (Part 1)

This project is a Wordle-based adaptation of Bulls and Cows.
Instead of digits, players guess 5-letter English words.

After each guess, the game shows:

color feedback:

🟩 green = correct letter, correct position\
🟨 yellow = correct letter, wrong position\
⬛ black/grey = letter not in the word

The number of remaining valid candidate words
The entropy associated with the remaining search space

```
Entropy Formula:
H = log2(N)
```

Where N = number of possible words remaining.

This tells the player how uncertain the game still is after each guess.

Example Output\
Enter 5-letter guess: meows\
🟨 M ⬛ E 🟨 O ⬛ W ⬛ S

Remaining words: 215

Entropy Calculation:
  H = log2(N)
  N = 215 (remaining possible words)
  H = log2(215) = 7.7482 bits

Entropy always decreases as the game gets closer to the answer.

🧠 Optimal Strategy Using Entropy (Part 2)

To develop the best strategy, the program evaluates each possible guess using mutual information:

Mutual Information Formula:
MI = H_before - E[H_after]

Meaning:
The guess that most evenly splits the remaining possibilities
Has the highest mutual information
And therefore gives the largest expected entropy reduction
The game automatically computes MI and suggests the best next guess.

Strategy:
Start with a guess that maximizes expected information gain
Use Wordle feedback to filter incompatible words
Choose the next guess with the highest MI
Repeat until entropy reaches zero and the word is found
This strategy consistently finds the word in very few guesses.


💡 Hint System (Added Feature)

When the game narrows to exactly one candidate word:

Hint 1 → Jumbled letter set

Example:
```
Possible letters: m, y, k, i, c
```

Hint 2 — Masked word pattern
```
m_c_y
```
After 2 failed attempts post-hints:
You've used both hints and made 2 incorrect attempts.
Do you want to reveal the secret word? (yes/no):

This preserves difficulty while offering structured assistance.


🖥️ User Interface (CLI)

The game uses a clean terminal-based interface, which satisfies the exam requirement of providing a user interface.

Features:
Immediate colored output under guesses
Easy-to-read entropy values
Guided prompts for hints & next steps
Replay option
