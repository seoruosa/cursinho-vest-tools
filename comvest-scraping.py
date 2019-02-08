import requests
from bs4 import BeautifulSoup
from collections import deque
from urllib.parse import urlparse, urlunparse, ParseResult
from general import *
from time import sleep
from random import random
import pickle

HOST = "http://www2.comvest.unicamp.br/" #/vestibulares-anteriores/1a-fase-2a-fase-comentadas/


# lists with links to the website
all_visited_pages=set()
have_to_visit = deque([HOST])

garbage_links = set()
all_links = {HOST}
file_links = set()

n = 0
while len(have_to_visit)>0:
	n += 1
#	if n>1:
#		break
	nextLink = have_to_visit.popleft()
	all_visited_pages.add(nextLink)
	print(nextLink)

	try:
		sleep(5 * (0.8+random()))
		page = requests.get(nextLink, timeout=5)
		soup = BeautifulSoup(page.content, 'html.parser')
	except:
		garbage_links.add(nextLink) # link that can´t visit
		soup = ''

	if soup != '':
		for link in soup.find_all():
			link_string = link.get('href')
			if(link_string != None):
			    link_string = extractLocationPath(link_string, HOST)

			    all_links.add(link_string)
			    if hasFileAtLink(link_string):
			    	file_links.add(link_string)
			    	print("file -----{}".format(link_string))
			    elif((link_string not in all_visited_pages) & isSubPageOfLocation(link_string, HOST)):
			    	have_to_visit.append(link_string)
			    	print("page -----{}".format(link_string))

	print("have_to_visit: {:d}".format(len(have_to_visit)))

filename = 'results.pickle'
with open(filename, 'wb') as f:
	pickle.dump({'garbage_links': garbage_links, 
				'all_links': all_links, 
				'file_links':file_links,
				'iterations':n}, f)

# http://www.jessicayung.com/how-to-use-pickle-to-save-and-load-variables-in-python/

# how to discovery if a link connect to the same website
# discovery if a link appoint to a file
# deal with links like this /unicamp/noticias/2018/05/19/comeca-upa-2018


