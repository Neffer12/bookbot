def word_count(text):
    words = []
    words = text.split()
    return len(words)

def character_count(text):
    lower = text.lower()
    character = {}
    for char in lower:
        if char in character:
            character[char] = character[char] + 1
        else:
            character[char] = 1
    return character