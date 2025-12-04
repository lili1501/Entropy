
"""
WORDLE WITH ENTROPY
Author: Shesadree Priyadarshani
Date: 12/03/2025

This script implements:
1. Wordle-style guessing game
2. Entropy calculation after every guess
3. Mutual-information strategy to suggest the best next guess
4. Two-tier hint system when only one possible word remains
5. Replay functionality for multiple game sessions

"""


import random
from functions import *
from calc_entropy import *

def main():

    # If the user wants to play multiple games (replay functionality)
    while True:   
        words = load_words()
        possible_words = words.copy()

        secret = random.choice(words)
        guess_count = 0
        first_hint_used = False
        second_hint_used = False
        failed_attempts_after_hints = 0

        print("\nWORDLE — GUESS THE WORD\n")

        # Actual game beginning
        while True:
            guess = input("\nEnter 5-letter guess: ").lower()

            if guess not in words:
                print("Not a valid word.")
                continue

            guess_count += 1

            fb = feedback(secret, guess)

            # Print colored feedback directly under the guess
            print()
            print_colored_feedback(guess, fb)
            print()

            # Update candidate list
            possible_words = filter_words(possible_words, guess, fb)

            # User guessed correctly
            if guess == secret:
                print("\nHurray! You solved it!")
                print(f"The secret word was: {secret.upper()}")
                print(f"You solved it in {guess_count} guesses!")
                break  # End current game session

            # Entropy calculation
            H = compute_entropy(possible_words)
            print(f"Remaining words: {len(possible_words)}")
            print_entropy_details(len(possible_words), H)
            print(f"Current Entropy: {H:.4f} bits")

            '''if only 1 word remains, let the user first try to guess it 
            and then offer a hint if they want it'''

            if len(possible_words) == 1:
                final_word = possible_words[0]

                print("\nOnly 1 possible word remains!")

                # jumbled letters of the final word
                if not first_hint_used:
                    choice = input("Do you want a hint? (yes/no): ").strip().lower()

                    if choice in ["yes", "y"]:
                        letters = possible_letter_set(possible_words)
                        print("\nPossible letters:", ", ".join(letters))
                        first_hint_used = True
                    else:
                        print("Okay! Try to guess the final word!")
                    continue

                # Second hint masked pattern of the word
                if not second_hint_used:
                    choice = input("Do you want another hint? (yes/no): ").strip().lower()

                    if choice in ["yes", "y"]:
                        hint = make_hint(final_word)
                        print("\nHere is your hint:", hint)
                        second_hint_used = True
                    else:
                        print("Alright! Give it another try!")
                    continue

                '''Count failed attempts after both hints used
                and then offer to reveal the word'''

                failed_attempts_after_hints += 1

                if failed_attempts_after_hints >= 2:
                    reveal = input("\nYou've used both hints and made 2 incorrect attempts.\n"
                                   "Do you want to reveal the secret word? (yes/no): "
                                   ).strip().lower()

                    if reveal in ["yes", "y"]:
                        print("\n🔍 The secret word is:", final_word.upper())
                        print(f"You solved it in {guess_count} guesses (with reveal).")
                        break
                    else:
                        print("Okay! Try again!")
                        continue

                print("No more hints available! Try to guess the final word!")
                continue

            if len(possible_words) > 1:
                bg, mi = best_guess(possible_words)
                print(f"Suggested next guess: {bg}\n(Mutual Information: {mi:.4f})")

        again = input("\nDo you want to guess another word? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("\nThanks for playing! You Played Well!")
            break   

if __name__ == "__main__":
    main()