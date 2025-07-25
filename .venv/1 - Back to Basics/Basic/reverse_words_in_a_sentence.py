def reverse_words_in_a_sentence():
    text = input("Enter a sentence that you would like to flip: ").split()
    text.reverse()
    reversed_text = ' '.join(text)
    print(f"{reversed_text}")

reverse_words_in_a_sentence()
