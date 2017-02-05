from googleapiclient.discovery import build
import pprint

class Search:
    def __init__(self):
        self._my_api_key = "AIzaSyAjPcYfHVtTbE5QjsapKaPOAazBULRQxis"
        self._my_cse_id = "016486028690415270981:qlzofnni66w"

    def google_search(self,search_term, **kwargs):
        service = build("customsearch", "v1", developerKey=self._my_api_key)
        res = service.cse().list(q=search_term, cx=self._my_cse_id, **kwargs).execute()
        links = []
        print res['searchInformation']['totalResults']
        for i in res['items']:
            links.append(i['link'])
        return links

# results = google_search(
#     'dangal full movie online', my_api_key, my_cse_id, num=10)
# for result in results:
#     pprint.pprint(result)