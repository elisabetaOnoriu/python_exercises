import string
from collections import Counter

filename = input("Enter filename (e.g. sample.txt): ")

with open(filename, 'r', encoding='utf-8') as f:
    text = f.read().lower()  # convert to lowercase

letters_only = ''.join(filter(str.isalpha, text))
letter_freq = Counter(letters_only)

translator = str.maketrans('', '', string.punctuation)
clean_text = text.translate(translator)
words = clean_text.split()
word_freq = Counter(words)

print("\nLetter Frequency:")
for letter, count in sorted(letter_freq.items()):
    print(f"{letter}: {count}")

print("\nWord Frequency:")
for word, count in word_freq.most_common():
    print(f"{word}: {count}")
