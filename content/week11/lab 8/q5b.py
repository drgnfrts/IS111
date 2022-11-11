from q5a import count_words_in_file

count = count_words_in_file("spam_sms.txt")
for word, num in count.items():
    if len(word) >= 4 and num > 50:
        print(f"{word} : {num}")
