
def movie_check(movies, year):
    if (year < 2000):
        print("This movie was released before 2000")
    else:
        print("This movie was released after 2000")
        return movies
def main():

    recent_movies = []

    favorite_movies = {
        ("Oppenheimer", 2023),
        ("Monsters INC", 2001),
        ("All Quiet on The Western Front", 1930),
        ("Superbad", 2007),
        ("Lion King", 1984)
    }



    for movies, year in favorite_movies:
        i = movie_check(movies, year)
        if i is not None:
            recent_movies.append(i)

    print(recent_movies)

main()