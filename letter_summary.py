
user_word = input("Please enter a word: ")

letter_histogram = {}

for letter in user_word:
    # print(letter)
    if not letter in letter_histogram:
        letter_histogram[letter] = 1
    if letter in letter_histogram:
        letter_histogram[letter] += 1

print(letter_histogram)