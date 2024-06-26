import pandas
import numpy
import boto3
from imdb import Cinemagoer

# Create an instance of the Cinemagoer class
instance = Cinemagoer()

print("-----------------------------------------------------------------------------------------")

# Get the movie name from the user
movie_name = input("Enter the full movie name: ")

# Search for the movie
movies = instance.search_movie(movie_name)
if movies:
    # Get the first movie (you can adjust this based on your requirements)
    movie_id = movies[0].movieID
    movie_info = instance.get_movie(movie_id, info=['main'])

    # Extract and format the names of the people involved
    def get_names(person_list):
        return [person['name'] for person in person_list] if person_list else 'N/A'
    
    # Print relevant information
    print(f"Title: {movie_info.get('title')}")
    print(f"IMDb Rating: {movie_info.get('rating')}")
    print(f"Released Year: {movie_info.get('year')}")
    print(f"Genre: {movie_info.get('genre')}")
    print(f"Language: {movie_info.get('language')}")
    print(f"Director: {', '.join(get_names(movie_info.get('directors')))}")
    print(f"Producer(s): {', '.join(get_names(movie_info.get('producer')))}")
    print(f"Cast: {', '.join(get_names(movie_info.get('cast')[:5]))}")
    print(f"Writer(s): {', '.join(get_names(movie_info.get('writers')))}")
    print(f"Storyline: {movie_info.get('Storyline')}")

else:
    print(f"Sorry, No movie found for '{movie_name}', the given name is either incorrect nor it does not have sufficient information...")

print("-----------------------------------------------------------------------------------------")
