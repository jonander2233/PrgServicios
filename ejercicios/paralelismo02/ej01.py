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
        # self.url coge el "url" que se le pase al constructor a la hora de llamar al metodo
        response = requests.get(self.url)






