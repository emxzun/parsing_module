import requests

from .settings import headers
from bs4 import BeautifulSoup


class Parser:

    def __init__(self, url):
        self.url = url

    def get_html(self):
        src = requests.get(url=self.url, headers=headers)
        return src.text

    def get_soup(self):
        soup = BeautifulSoup(self.get_html(), 'lxml')
        return soup
