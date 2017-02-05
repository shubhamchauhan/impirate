from search import Search
from VideoSource import VidSource
from Browser import Browse

a = Browse()
b = Search()
query = raw_input("Please enter a movie name : ")

final_results = []

search_results = b.google_search(query)
print search_results
for i in search_results:
	c = VidSource(i,query)
	links = c.getResults()
	d = a.run(links)
	if len(d)>0:
		for j in d:
			final_results.append(j)

print(final_results)
