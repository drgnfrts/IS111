import random


def scramble_word(word):
    # there is no need to scramble words that are 3 characters or less in length, return them directly
    if len(word) <= 3:
        return word
    # initialise list of exceptions, and prepare an empty list to store tuples of (index, exception)
    punctuation = ",'!.:"
    punctuation_index = []
    letters = []
    # if punctuation is at the back of the word, we don't want it inside. store it to put back later
    if word[-1] in punctuation:
        back_punctuation = word[-1]
        clean_word = word[:-1]
    else:
        back_punctuation = ""
        clean_word = word
    # dump the non-punctuation middle characters into the list "letters"
    # for punctutation, send (index, punctutation) to the list "punctuation_index"
    for i in range(1, len(clean_word) - 1):
        if word[i] in punctuation:
            punctuation_index.append((i, clean_word[i]))
        else:
            letters.append(clean_word[i])
    # shuffle the middle characters
    random.shuffle(letters)
    # using the stored list of (index, punctuation), reinsert the punctuation
    for punctuation_tuple in punctuation_index:
        letters.insert(punctuation_tuple[0], punctuation_tuple[1])
    # generate the number of unique letters in the middle for the recursion check later
    unique_letters_inside = len(list(set(letters)))
    # insert the front and back letters and join back the word
    letters.insert(0, clean_word[0])
    letters.insert(len(clean_word) - 1, clean_word[len(clean_word) - 1])
    new_word = "".join(letters)
    # re-generate a shuffled word if the new word is same as the original
    # however, do not regenerate if unique letters inside = 1 (e.g. "need") because it will cause the function to run forever
    if unique_letters_inside != 1:
        while new_word == clean_word:
            # uncomment the line below to see if we need to re-shuffle
            print(
                f"RECURSION ACTIVATED for {new_word}: duplicates {clean_word}")
            new_word = scramble_word(clean_word)
    # add back the back punctuation, if any
    returned_word = new_word + back_punctuation
    return returned_word


sentence_list = []
with open("talk.txt", "r") as input_file:
    for line in input_file:
        stripped = line.strip("\n").split()
        sentence_list.append(stripped)
for sentence in sentence_list:
    for k in range(len(sentence)):
        sentence[k] = scramble_word(sentence[k])
    print(" ".join(sentence))
