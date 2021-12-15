FILENAME = "movie_list.txt"


def write_movies(movies):
    with open(FILENAME, "w") as file:
        for movie in movies:
            file.write(movie + "\n")


def read_movies():
    movies = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
            return movies


def list_movies(movies):
    #print(len(movies))
    for i in range(len(movies)):
        movie = movies[i]
        print(str(i + 1) + ". " + movie)



def add_movies(movies):
    movie = input("Movie:")

    movies.append(movie)
    write_movies(movies)
    print(movie + " was added.\n")


def delete_movies(movies):

    index = int(input("Number: "))
    index=index-1
    if index<len(movies):
        movie = movies.pop(index)
        write_movies(movie)
        print(movie + " was deleted.\n")
    else:
        print("No Movie at this number Mukesh G!!!")


def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("search -  To Search a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()


def search_movies(movies):
    movie=input("enter movie name you want to search--" + "\n")
    file1=open("movie_list.txt", "r")
    readfile=file1.read()
    #print(readfile)
    if movie in readfile:  # never use readfile()
        #print(movie.index(movie))
        place=movies.index(movie)
        print(place)
        #place=movies.index(movie)
        print(movies[place])
        print("Your Search movie ",  movie , " is available")
        
    else:
        
        print("Not found Mukesh Canada waleya..")

    file1.close()
    


def main():
    display_menu()
    movies = read_movies()
    while True:
        command = input("Command: ")
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movies(movies)
        elif command == "del":
            delete_movies(movies)
        elif command == "search":
            search_movies(movies)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again. mukesh g hor theek thak ho sadi yaad ni andi")

if __name__ == "__main__":
    
    main()
