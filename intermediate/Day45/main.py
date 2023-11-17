from bs4 import BeautifulSoup
import requests


response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
print(soup.title)
print()

article_texts = []
article_links = []
articles = [span.find('a') for span in soup.find_all(name='span', class_='titleline')]

for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get('href'))

article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]
print(article_scores)
print(len(article_scores))
print(len(article_texts))
print(max(article_scores))
highest_score = max(article_scores)
highest_article_score_index = article_scores.index(highest_score) + 1
print(highest_article_score_index)

print(article_texts[highest_article_score_index])
print(article_links[highest_article_score_index])

# with open('website.html', 'r', encoding='utf-8') as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'lxml')
# print(soup.title)