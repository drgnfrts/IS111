'''
E1)
Write a function called reverse_words() that takes in a piece of text that consists of multiple words. The function returns a string that is a transformed version of the text where each word is reversed. 

You can assume that the words in the given text are separated by spaces, i.e., there is a single space between two adjacent words.

For example, reverse_words("I study at SMU") returns "I yduts ta UMS". reverse_words("Python is a programming language.") returns "nohtyP si a gnimmargorp .egaugnal". If the input text is an empty string, the function returns an empty string.
'''


def reverse_words(input_string):
    if len(input_string) == 0:
        return ""
    return_string = []
    broken_up_sentence = input_string.split(" ")
    for word in broken_up_sentence:
        return_string.append(word[::-1])
        # use append not concat
    return " ".join(return_string)


print(reverse_words("I study at SMU"))
