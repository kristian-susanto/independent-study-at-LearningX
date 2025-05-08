import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('mongodb+srvnWypAXritSE3nkERULGu0L59UJr6qzKX@learningx.6fl0g.mongodb.netretryWrites=true&w=majority&appName=LearningX')
db = client.dbpretest2

# Mengambil HTML
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# Link scraping
url = 'https://www.bilibili.tv/id/anime'

# Menggunakan requests library
data = requests.get(url=url, headers=headers)

# Menggunakan library BeautifulSoup
soup = BeautifulSoup(data.text, 'html.parser')

# Menggunakan select
animes = soup.select('li > .bstar-video-card')
# print('Jumlah data:', len(animes))

# Looping
for anime in animes:
    # Mengambil judul
    title = anime.select_one('.bstar-video-card__text-wrap > .bstar-video-card__text > .bstar-video-card__text-content > p').text.strip()
    # Mengambil genre
    genre = anime.select_one('.bstar-video-card__text-wrap > .bstar-video-card__text > .bstar-video-card__text-content > .bstar-video-card__text-desc > p').text.strip()
    genre = genre.split('· ')
    genre = "{}".format(genre[1])
    # Mengambil gambar
    cover = anime.select_one('img', class_='bstar-image__img')['src']
    cover = cover.split('@')[0]
    # Melakukan pencetakan
    # print(title, '|', genre, '|', cover)
    # Memasukkan data
    # doc = {
    #     'title' : title,
    #     'genre' : genre,
    #     'cover' : cover
    # }
    # db.animes.insert_one(doc)