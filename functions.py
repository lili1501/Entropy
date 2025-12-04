
import random


def load_words():
    with open("valid_words.txt") as f:
        words = [w.strip().lower() for w in f if len(w.strip()) == 5]
    return words

def count_letters(word):
    freq = {}
    for ch in word:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1
    return freq


def feedback(secret, guess):
    result = ["B"] * 5

    # manual frequency count
    secret_freq = {}
    for ch in secret:
        secret_freq[ch] = secret_freq.get(ch, 0) + 1

    # Greens (correct position)
    for i in range(5):
        if guess[i] == secret[i]:
            result[i] = "G"
            secret_freq[guess[i]] -= 1

    # Yellows (correct letter, wrong place)
    for i in range(5):
        if result[i] == "B":
            letter = guess[i]

            # ✔ FIX: check if letter exists before accessing
            if letter in secret_freq and secret_freq[letter] > 0:
                result[i] = "Y"
                secret_freq[letter] -= 1

    return "".join(result)


def filter_words(words, guess, fb):
    filtered = []
    for w in words:
        if feedback(w, guess) == fb:
            filtered.append(w)
    return filtered



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

def make_hint(word):
    n = len(word)
    mid = n // 2  # middle index

    hint = ""
    for i, ch in enumerate(word):
        if i == 0 or i == mid or i == n - 1:
            hint += ch
        else:
            hint += "_"
    return hint

def possible_letter_set(candidates):
    letter_set = set()
    for word in candidates:
        for ch in word:
            letter_set.add(ch)

    letters = list(letter_set)
    random.shuffle(letters)   
    return letters