trie = {}

def insert(word):
    node = trie
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node['*'] = True

def search(word):
    node = trie
    for char in word:
        if char not in node:
            return False
        node = node[char]
    return '*' in node

def starts_with(prefix):
    node = trie
    for char in prefix:
        if char not in node:
            return False
        node = node[char]
    return True

print("Commands: insert, search, prefix, quit")

while True:
    command = input("Enter command: ").strip().lower()

    if command == "insert":
        word = input("Word to insert: ").strip().lower()
        insert(word)
        print(f"Inserted '{word}'.")

    elif command == "search":
        word = input("Word to search: ").strip().lower()
        print("Found." if search(word) else "Not found.")

    elif command == "prefix":
        prefix = input("Prefix to check: ").strip().lower()
        print("Prefix exists." if starts_with(prefix) else "No word with that prefix.")

    elif command == "quit":
        print("Bye!")
        break

    else:
        print("Unknown command. Use: insert, search, prefix, quit.")
