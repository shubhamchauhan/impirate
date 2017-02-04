#import urllib
import requests
from bs4 import BeautifulSoup

url = 'http://www.kumby.com/avatar-the-last-airbender-book-3-chapter-5/'

source_object = requests.get(url)
soup = BeautifulSoup(source_object.text, 'html.parser')
k = soup.prettify()
#print(k)
important = soup.findAll("embed","object","param","video")
print(len(important))
for i in important:
	print(i)