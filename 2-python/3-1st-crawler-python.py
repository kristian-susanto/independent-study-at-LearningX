import requests
from bs4 import BeautifulSoup

# Baca URLnya dan ambil HTMLnya,
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# Kamu akan memulai "scraping" dari data pada halaman ini
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

# Gunakan requests library untuk mendapatkan kode HTML dari link diatas
data = requests.get(url=url, headers=headers)

# library BeautifulSoup memudahkan kita dalam
# menguraikan kode HTML tersebut,
soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('ul.ipc-metadata-list > li')

# for movie in movies:
    # movie_title = movie.select_one('div.ipc-title > a > h3').text.strip()
    # movie_title = movie_title.split('. ')
    # movie_title = "{}".format(movie_title[1])
    # year = movie.select_one('.cli-title-metadata > span').text.strip()
    # rating = movie.select_one('.cli-ratings-container > span').text.strip()
    # rating = rating.split('\xa0')
    # rating = "{}".format(rating[0])
    # print(movie_title, '/', year, '/', rating)

for film in movies:
    judul = film.select_one('.ipc-title__text').text
    judul = judul.split('. ')
    judul = "{}".format(judul[1])
    tahun = film.select_one('.sc-b0691f29-7 > .sc-b0691f29-8').text
    rating = film.select_one('.ipc-rating-star').contents[1].text
    print(judul,'-',tahun,'-',rating)