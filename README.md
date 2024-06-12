# IMDb-Movie-Search

## Description
This project uses IMDbPY to search for movies and retrieve major information including cast, genres, year of release, rating, run time, languages, director, writer, and plot. The project is containerized using Docker and integrated with AWS for storage and deployment.

## Technologies Used
- Python
- IMDbPY
- Pandas
- NumPy
- AWS (S3, Lambda, EC2)
- GitHub
- Linux

## How to Run
1. Clone the repository.
2. For example, The application will search for the movie "Inception" and print the information.
5. Results are uploaded to the specified S3 bucket.


# Set Up the Environment:

# Step 1: Install IMDbPY: You can install IMDbPY via pip. (I used "bash" as Scripting)
pip install IMDbPY

# Step 2: Install other dependencies

pip install pandas numpy boto3

# Step 3: Set up a GitHub repository on GitHub, and clone the repository to your local machine.

# git clone https://github.com/jibinjohny93/IMDb-Movie-Search.git ----> clone the repository

# git add .\python-code.py                    ---> add the code to staging area
# git commit -m "imported the imdb library"   ---> commit the code
# git push                                    ---> push the code
# git status                                  ---> check the changes to commit


