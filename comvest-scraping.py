import requests
from bs4 import BeautifulSoup
from collections import deque

host = "http://www.comvest.unicamp.br" #/vestibulares-anteriores/1a-fase-2a-fase-comentadas/

# lists with links to the website
all_visited_pages=set()
have_to_visit = deque([host])

garbage_links = set()
all_links = {host}


while len(have_to_visit)>0:
	host = have_to_visit.popleft()
	all_visited_pages.add(host)
	print(host)

	try:
		page = requests.get(host, timeout=5)
		soup = BeautifulSoup(page.content, 'html.parser')
	except:
		garbage_links.add(host)
		soup = ''

	if soup != '':
		for link in soup.find_all():
		    link_string = link.get('href')

		    all_links.add(link_string)
		    if ((link_string not in all_visited_pages) and (link_string != None)):
		    	have_to_visit.append(link_string)

	print("have_to_visit: {:d}".format(len(have_to_visit)))

# how to discovery if a link connect to the same website
# discovery if a link appoint to a file
# deal with links like this /unicamp/noticias/2018/05/19/comeca-upa-2018