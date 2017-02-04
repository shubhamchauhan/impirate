import requests
from bs4 import BeautifulSoup

url = 'http://hindimoviesonline.watch/dangal-full-movie-online/'

source_object = requests.get(url)
soup = BeautifulSoup(source_object.content, 'html.parser')
#tag = soup.findall('video', {'class':'jw-video jw-reset'})
print(soup.prettify())
