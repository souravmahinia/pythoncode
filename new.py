def search_movies():
    movie=input("enter movie name you want to search")
    file=open("movielist.txt", "r")
    readfile=file.read()
    if movie in readfile():
        print("your search movie" + str.movie+ "found in movie list Mukesh G!!!!")

    else:
        print("Not found Mukesh Canada waleya..")

    file.close()

if __name__ == "__main__":
    search_movies()