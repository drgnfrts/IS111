def extract_bold_texts(html_text):
    r_list = []
    split = html_text.split("<b>")
    split.pop(0)
    for line in split:
        further = line.split("</b>")
        r_list.append(further[0])
    return r_list


print(extract_bold_texts('<b>ABC</b> abc <b>def 123 </b><b></b>0000'))
print(extract_bold_texts('A piece of text without tags.'))
