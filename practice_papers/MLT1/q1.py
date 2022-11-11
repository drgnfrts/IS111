# =====
# q1.py
# =====
# Name: Tang Wen Chung, Nicolas
# Email ID: nicolastang.2022

def get_hashtags(post_list):
    hashtag_list = []
    for post in post_list:
        holding_list = []
        holding_list = post.split()
        for words in holding_list:
            if words[0] == "#":
                hashtag_list.append(words)
    return hashtag_list
