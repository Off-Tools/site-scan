from bs4 import BeautifulSoup
import requests
import re
class Engine:

    def __init__(self, url):
        self.url = url
        self.header = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

    def get_urls(self):

        req = requests.get(self.url, self.header)
        soup = BeautifulSoup(req.content, 'html.parser')
        links = soup.find_all("a", href=True)
        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', str(links))
        return urls


if __name__ == "__main__":
    engine = Engine('https://gatefy.com')
    print(engine.get_urls())