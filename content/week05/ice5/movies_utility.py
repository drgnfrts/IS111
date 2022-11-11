def get_average_duration(list_of_tuples):
    if len(list_of_tuples) == 0:
        return 0.0
    total_duration = 0
    for movie_tuple in list_of_tuples:
        total_duration += movie_tuple[2]
    return total_duration / len(list_of_tuples)


def get_num_movies_of_genre(list_of_tuples, genre):
    # if len(list_of_tuples) == 0:
    # return 0
    num_of_movies = 0
    for movie_tuple in list_of_tuples:
        if movie_tuple[1] == genre:
            num_of_movies += 1
    return num_of_movies


def get_title_of_longest_movie(list_of_tuples):
    longest_movie_title = ""
    for movie_tuple in list_of_tuples:
        if len(movie_tuple[0]) > len(longest_movie_title):
            longest_movie_title = movie_tuple[0]
    return longest_movie_title


def get_movies_with_keyword(list_of_tuples, keyword):
    list_of_keyword_movies = []
    for movie_tuple in list_of_tuples:
        if keyword in movie_tuple[0]:
            list_of_keyword_movies.append(movie_tuple[0])
    return list_of_keyword_movies
