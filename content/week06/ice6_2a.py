def get_unique_titles(list_of_tuples):
    unique_titles = []
    for indiv_tuple in list_of_tuples:
        title, edition, cover, copies = indiv_tuple
        if title not in unique_titles:
            unique_titles.append(title)
    return unique_titles


print(get_unique_titles([("Intro to Programming", "Ed-2", "paperback", 2), ("Intro to Python",
      "Ed-1", "paperback", 5), ("Intro to Programming", "Ed-3", "hardcover", 4)]))
