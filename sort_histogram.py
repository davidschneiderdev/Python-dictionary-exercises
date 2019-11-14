
user_sentence = input("Please enter a sentence: ")

def word_histogram(user_sentence):
    
    word_list = user_sentence.lower().split()
    # print(word_list)

    word_histogram = {}

    for word in word_list:

        if word not in word_histogram:
            word_histogram[word] = 1
        elif word in word_histogram:
            word_histogram[word] += 1

    return word_histogram

# print(word_histogram(user_sentence))
result_histogram = word_histogram(user_sentence)
# print(result_histogram)

sorted_histogram = sorted(result_histogram.items(), key=lambda value: value[1], reverse=True)
# sorted(result_histogram.values(), reverse=True))
first_rank = sorted_histogram[0]
second_rank = sorted_histogram[1]
third_rank = sorted_histogram[2]

# print(result_histogram[first_key])
print("The top three words are: ")
print(first_rank)
print(second_rank)
print(third_rank)

    
    
    





