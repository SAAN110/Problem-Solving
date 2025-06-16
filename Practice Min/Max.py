def find_min_max(t): 
    if not t: 
        return None, None     
    min_value = min(t)     
    max_value = max(t)     
    return min_value, max_value 
numbers_tuple = (5, 12, 7, 1, 9, 20, 3) 
min_val, max_val = find_min_max(numbers_tuple) 
print(f"Minimum value: {min_val}") 
print(f"Maximum value: {max_val}") 

def count_letter_occurrences(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

word = "MISSISSIPPI"
letter_count = count_letter_occurrences(word)
print(f"Letter counts in '{word}': {letter_count}")

user_word = input("Enter a word: ")
user_letter_count = count_letter_occurrences(user_word)
print(f"Letter counts in '{user_word}': {user_letter_count}")
