import requests

from bs4 import BeautifulSoup

url = "https://www.imdb.com/search/keyword/?keywords=anime"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content,"html.parser")

titles = soup.find_all("h3",{"class":"lister-item-header"})
likes = soup.find_all("div",{"class":"inline-block ratings-imdb-rating"})

for title, like in zip(titles,likes):
    title = title.text
    like = like.text

    title = title.strip()
    title = title.replace("\n","")
    like = like.strip()
    like = like.replace("\n","")
    print("Title :",title)
    print("Likes :",like)