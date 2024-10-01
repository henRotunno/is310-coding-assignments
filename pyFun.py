
def movie_book():

    favorites = [ 
    {
    "Movie": "Oppenheimer, 2023",
    "Book": "All Quiet on The Western Front, The Road Back"
    }
    ]
    inputs(favorites)

def inputs(movie_book):

    user_inp_movie = input("Enter your favorite movie: ")
    user_inp_book = input("Enter your favorite book: ")

    movie_book.append(user_inp_movie)
    movie_book.append(user_inp_book)
    print(movie_book)
    
def main():
    movie_book()
        

main()


