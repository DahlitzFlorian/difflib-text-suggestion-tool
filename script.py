from __future__ import annotations
import difflib


def get_dictionary() -> set[str]:
    with open("core-wordnet.txt") as f:
        data = f.readlines()
    
    words = [
        line.split()[2][1:-1]
        for line in data
    ]

    return set(words)


def suggest(phrase: str) -> tuple[int, str]:
    changes = 0
    words = phrase.split()
    dictionary = get_dictionary()
    
    for idx, word in enumerate(words):
        if word not in dictionary:
            changes += 1
            matches = difflib.get_close_matches(word, dictionary)
            
            if matches:
                words[idx] = matches[0]
    
    return changes, " ".join(words)


if __name__ == "__main__":
    phrase = input("Your phrase: ")
    number_changes, adjusted_phrase = suggest(phrase)
    print(f"Number of changes: {number_changes}")
    print(f"Adjusted Phrase: {adjusted_phrase}")
    print(f"Original Phrase: {phrase}")
