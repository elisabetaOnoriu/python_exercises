class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        dictionary = self.trie

        for character in word:
            if character not in dictionary:
                dictionary[character] = {}
            dictionary = dictionary[character]

        dictionary["."] = "."

    def search(self, word: str) -> bool:
        dictionary = self.trie
        for character in word:
            if character not in dictionary:
                return False
            dictionary = dictionary[character]

        return "." in dictionary

    def starts_with(self, prefix: str) -> bool:
        dictionary = self.trie
        for character in prefix:
            if character not in dictionary:
                return False
            dictionary = dictionary[character]

        return True


trie = Trie()
trie.insert("cat")
trie.insert("car")

print(trie.trie)
print(trie.search("cat"))
print(trie.search("ca"))
print(trie.starts_with("ca"))
print(trie.starts_with("car"))
print(trie.starts_with("dog"))
