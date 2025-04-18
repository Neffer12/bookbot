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

def sort_on(dict):
    return dict["count"]

def sorted_list(character):
    result = []
    for char, count in character.items():
        char_dict = {"char": char, "count": count}
        result.append(char_dict)
    result.sort(reverse=True, key=sort_on)
    return result