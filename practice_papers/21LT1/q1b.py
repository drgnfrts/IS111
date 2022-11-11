# Name:
# Email ID:

official_languages = (("Belgium", ("Dutch", "French", "German")), ("Canada", ("English", "French")),
                      ("Phillipines", ("English", "Filipino")), ("Singapore", ("English", "Malay", "Chinese", "Tamil")))


def is_official_language(country, language):
    # Replace the code below with your implementation.
    for i in range(len(official_languages)):
        if official_languages[i][0] == country:
            for j in range(len(official_languages[i][1])):
                if language == official_languages[i][1][j]:
                    return True
    return False
