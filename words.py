def print_upper_words(list):
    for word in list:
        word = word.upper()
        print(word)

def print_letter_words(list, set):
    for letter in set:
        for word in list:
            if word[0] == letter:
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
print_letter_words(["hello", "hey", "goodbye", "yo", "yes"], {"h", "y"})
