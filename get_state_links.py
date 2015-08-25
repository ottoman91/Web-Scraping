from bs4 import BeautifulSoup
from urllib2 import urlopen

#URL that opens the first page from which school data for different states can be taken
BASE_URL = "http://www.city-data.com/indexes/schools/" 

data = [] # for storing school links and displaying them 


#function for getting the URL for states data on schools
def get_state_links(BASE_URL):
	html = urlopen(BASE_URL).read()
	soup = BeautifulSoup(html, "lxml")
	state_list = soup.find("ul","tab-list tab-list-short")
	state_links = [li.a["href"] for li in state_list.findAll("li")] 
	return state_links 

data.append(get_state_links(BASE_URL)) #for testing
print data #for testing
	

	
