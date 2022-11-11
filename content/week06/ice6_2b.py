def get_titles_and_counts(list_of_tuples):
    titles_and_counts = []
    for indiv_tuple in list_of_tuples:
        title, edition, cover, copies = indiv_tuple
        if titles_and_counts == []:
            titles_and_counts.append([title, copies])
        else:
            for sublist in titles_and_counts:
                if title == sublist[0]:
                    sublist[1] += copies
                    added = True
                    break
                else:
                    added = False
            if not added:
                titles_and_counts.append([title, copies])
    return titles_and_counts


print(get_titles_and_counts([("Intro to Programming", "Ed-2", "paperback", 2), ("Intro to Python", "Ed-1",
      "paperback", 5), ("Intro to Programming", "Ed-3", "hardcover", 4), ("Intro to Python", "Ed-3", "hardcover", 3)]))
