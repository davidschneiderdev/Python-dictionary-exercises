
user_sentence = input("Please enter a sentence: ")

word_list = user_sentence.lower().split()
# print(word_list)

word_histogram = {}

for word in word_list:
    # print(word)
    if word not in word_histogram:
        word_histogram[word] = 1
    elif word in word_histogram:
        word_histogram[word] += 1

print(word_histogram)