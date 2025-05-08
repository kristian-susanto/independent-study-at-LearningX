import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient            # Importing pymongo (You have to install the package first)
client = MongoClient('mongodb+srv://nWypAXritSE3nkER:ULGu0L59UJr6qzKX@learningx.6fl0g.mongodb.net/?retryWrites=true&w=majority&appName=LearningX')
db = client.dbsparta                      # Create a db named 'dbsparta'.

# Baca URLnya dan ambil HTMLnya
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# Kamu akan memulai "scraping" dari data pada halaman ini
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

# Gunakan requests library untuk mendapatkan kode HTML dari link diatas
data = requests.get(url=url, headers=headers)

# Library BeautifulSoup memudahkan kita dalam menguraikan kode HTML tersebut
soup = BeautifulSoup(data.text, 'html.parser')

# Menggunakan select
movies = soup.select('ul.ipc-metadata-list > li')

# Looping pada setiap filmnya
for movie in movies:
    # Pertama, mari kita ambil judul dari filmnya
    movie_title = movie.select_one('div.ipc-title > a > h3').text.strip()
    movie_title = movie_title.split('. ')
    movie_title = "{}".format(movie_title[1])
    # Lalu, mari kita ambil tahun perilisan film tersebut
    year = movie.select_one('.cli-title-metadata > span').text.strip()
    # Terakhir, Mari kita ambil rating dari tiap-tiap movies
    rating = movie.select_one('.cli-ratings-container > span').text.strip()
    rating = rating.split('\xa0')
    rating = "{}".format(rating[0])
    # ... dan print semua secara berdampingan!
    print(movie_title, '/', year, '/', rating)
    # doc = {
    #     'movie' : movie_title,
    #     'year' : year,
    #     'rating' : rating
    # }
    # db.movies.insert_one(doc)