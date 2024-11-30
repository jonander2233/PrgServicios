import threading
import requests
from bs4 import BeautifulSoup
import re

class MiScraping(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url = url
        self.links =[]
    def run(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text,"html.parser")
        self.links = [a['href'] for a in soup.find_all('a', href=True) if re.match(r'http[s]?://', a['href'])]
    def get_links(self):
        return self.links




