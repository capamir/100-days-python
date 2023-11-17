from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(BASE_URL)
empire_web_page = response.text
soup = BeautifulSoup(empire_web_page, 'html.parser')

# title
print(soup.title.getText().split(' | ')[0], end='\n\n')

movies = [movie_tag.getText() for movie_tag in soup.find_all(name='h3', class_='listicleItem_listicle-item__title__hW_Kn')]

with open('top_movies.txt', 'w', encoding='utf-8') as file:
    # Write each item from the list to a new line in the file
    for item in movies[::-1]:
        file.write("%s\n" % item)