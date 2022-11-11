def mask_out(sentence, banned, substitutes):
    new_str = ""
    if len(banned) > len(substitutes):
        revert_num = len(banned) - len(substitutes)
        substitutes += revert_num * substitutes[0]
    for ch in sentence:
        replaced = False
        for i in range(len(banned)):
            if ch == banned[i]:
                new_str += substitutes[i]
                replaced = True
        if not replaced:
            new_str += ch
    return new_str


print(mask_out('pineapple', 'e', '#'))
print(mask_out('pineapple', 'aeiou', '#$%^&'))
print(mask_out('pineapple', 'aeiou', '#$'))
