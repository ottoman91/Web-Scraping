from bs4 import BeautifulSoup
from urllib2 import urlopen
import time
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

#data.append(get_state_links(BASE_URL)) #for testing
#print data #for testing
	
def get_school_info(state_url):
	html = urlopen(state_url).read()
	soup = BeautifulSoup(html,"lxml")
	state = soup.find("h1","city").string  
	school_data_table = soup.find("div","table-responsive") 
	school_info = [td.string for td in school_data_table.findAll("td")]
	return school_info 

state_info = get_state_links(BASE_URL) 

for info_link in state_info:
	school_infos = get_school_info(info_link) 
	data.append(school_infos)
	

print data

