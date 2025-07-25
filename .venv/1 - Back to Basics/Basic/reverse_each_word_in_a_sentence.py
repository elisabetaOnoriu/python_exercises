def reverse_words_in_a_sentence():
    text = input("Enter a sentence to flip each word backwards.: ").split()
    for index, word in enumerate(text):
        text[index] = word[::-1]
    text = ' '.join(text)
    print(f"{text}")

reverse_words_in_a_sentence()
