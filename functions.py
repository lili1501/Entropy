
'''Used the valid_words.txt file from online github source available at:
   https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93'''

import random

# Load valid 5 letter words from valid_words.txt file
def load_words():
    with open("valid_words.txt") as f:
        words = [w.strip().lower() for w in f if len(w.strip()) == 5]
    return words

# A frequency counter for letters in a word
def count_letters(word):
    freq = {}
    for ch in word:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1
    return freq


''' It helps user by providing feedback for a guess against the secret word
    if the letter for the guess 5 letter word is in the correct position -> G (green),
    if the letter is in the word but wrong position -> Y (yellow) and 
    if the letter is not in the word -> B (black/gray)'''
def feedback(secret, guess):
    result = ["B"] * 5

    # manual frequency count
    secret_freq = {}
    for ch in secret:
        secret_freq[ch] = secret_freq.get(ch, 0) + 1

    # Greens -> correct letter, correct position
    for i in range(5):
        if guess[i] == secret[i]:
            result[i] = "G"
            secret_freq[guess[i]] -= 1

    # Yellows -> correct letter, wrong place 
    for i in range(5):
        if result[i] == "B":
            letter = guess[i]

            # check if the letter exists before accessing
            if letter in secret_freq and secret_freq[letter] > 0:
                result[i] = "Y"
                secret_freq[letter] -= 1

    return "".join(result)


# Filters the possible words based on the feedback received
def filter_words(words, guess, fb):
    filtered = []
    for w in words:
        if feedback(w, guess) == fb:
            filtered.append(w)
    return filtered


# For user interface easy to detect with colored feedback
def print_colored_feedback(guess, pattern):
    GREEN = "\033[1;42m"
    YELLOW = "\033[1;43m"
    GRAY   = "\033[1;40m"
    RESET  = "\033[0m"
    out = ""
    for ch, fb in zip(guess, pattern):
        if fb == "G":
            out += f"{GREEN} {ch.upper()} {RESET}"
        elif fb == "Y":
            out += f"{YELLOW} {ch.upper()} {RESET}"
        else:
            out += f"{GRAY} {ch.upper()} {RESET}"
    print(out)

# When only one word remains, provide jumbled letters as a First hint to the user if asked
def possible_letter_set(candidates):
    letter_set = set()
    for word in candidates:
        for ch in word:
            letter_set.add(ch)

    letters = list(letter_set)
    random.shuffle(letters)   
    return letters


'''If the user still can't guess after the 1st hint provide 
   the second hint which reveals the first, middle, and last letters 
   of the final word if asked by the user'''

def make_hint(word):
    n = len(word)
    mid = n // 2  

    hint = ""
    for i, ch in enumerate(word):
        if i == 0 or i == mid or i == n - 1:
            hint += ch
        else:
            hint += "_"
    return hint

