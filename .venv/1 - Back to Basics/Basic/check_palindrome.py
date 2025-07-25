def check_palindrome():
    word = input("Insert a valid palindrome: ")
    reversed_word = word[::-1]
    if (word != reversed_word):
        print(f"{word} is just not the same as {reversed_word}.")
    else:
        print(f"Well done. {word} is a valid palindrome.")

check_palindrome()