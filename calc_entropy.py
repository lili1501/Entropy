
import math
from functions import *

def compute_entropy(words):
    n = len(words)
    if n == 0:
        return 0
    return math.log2(n)


# Calculate the Mutual information gain of a guess given the current possible words
def info_gain(guess, candidates):
    pattern_counts = {}

    for w in candidates:
        fb = feedback(w, guess)
        if fb not in pattern_counts:
            pattern_counts[fb] = 0
        pattern_counts[fb] += 1

    total = len(candidates)
    expected_entropy = 0

    for count in pattern_counts.values():
        p = count / total
        expected_entropy += p * math.log2(count)

    current_entropy = math.log2(total)
    return current_entropy - expected_entropy

# It helps user find the best guess word from the possible words list based on maximum information gain
def best_guess(candidates):
    best_word = None
    best_mi = -1

    for g in candidates:
        mi = info_gain(g, candidates)
        if mi > best_mi:
            best_mi = mi
            best_word = g

    return best_word, best_mi

# Print entropy calculation details to the user after each guess
def print_entropy_details(n, H):
    print("\nEntropy Calculation:")
    print(f"  H = log2(N)")
    print(f"  N = {n} (remaining possible words)")
    print(f"  H = log2({n}) = {H:.4f} bits\n")