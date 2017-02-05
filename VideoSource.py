
# coding: utf-8

# In[1]:

import requests
from bs4 import BeautifulSoup


# In[35]:

class VidSource(object):
    def __init__(self, url, query, keyclass = ['iframe','video','embed']):
        self.url = url
        self.soupa = ''
        self.links = []
        self.keys = keyclass
        self.count = 0
        self.query = query

    def __getUrlSource__(self, url):
        if "http" in url:
            source_object = requests.get(url)
            soup = BeautifulSoup(source_object.text, 'html.parser')
            return(soup)
        else:
            source_object = requests.get('http://csb.stanford.edu/class/public/pages/sykes_webdesign/05_simple.html')
            soup = BeautifulSoup(source_object.text, 'html.parser')
            return(soup)

    def _getLinks_(self, termlist, soup):
        for i in termlist:
            self._loadIframes_(i, soup)

    def _loadIframes_(self, i, soup):
        k = soup.findAll(i)
        self.count = self.count + 1
        if len(k)>0:
            for j in k:
                if j.has_attr('src') and j['src'] is None:
                    if self.count < 2:
                        try:
                            print j['src']
                            soupb = self.__getUrlSource__(j['src'])
                            self._getLinks_(['video', 'embed'], soupb)
                        except:
                            pass
                    else:
                        pass

                if j.has_attr('src') and j['src'] is not None:
                    self._filter_(j['src'])

    def _filter_(self, url):
        soup = self.__getUrlSource__(url)
        k = soup.findAll('<video>')
        if k is not None:
            self.links.append(url)

    def getResults(self):
        self.soupa = self.__getUrlSource__(self.url)
        self._getLinks_(self.keys, self.soupa)
        return(self.links)


# In[34]:

# if __name__ == '__main__':
#     address = 'http://hindimoviesonline.watch/dangal-full-movie-online/'
#     query = 'dangal'
#     k = VidSource(address, query)
#     print(k.getResults())


# In[ ]:




# In[ ]:
