import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response.raise_for_status()
em_webpage = response.text

soup = BeautifulSoup(em_webpage, "html.parser")
movie_data = soup.find_all(name="h3", class_="title")
movie_titles = [data.getText() for data in movie_data]

movie_titles_mod = movie_titles[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as movie:
    for title in movie_titles_mod:
        movie.write(title+"\n")
