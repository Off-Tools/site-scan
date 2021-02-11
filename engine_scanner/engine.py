from bs4 import BeautifulSoup
import requests
import re
#import payload
from engine_scanner.payload import payload_list
payload = payload_list
class Engine:
    def __init__(
self, url):
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
        # debuging..
        # arq = open('engine_scanner/response.txt', 'w', encoding='utf8')
        # arq.write(req.text)

        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', str(req.text))
        print(urls)
        return urls


    def check_ssrf(self, urls):
        dicionario_resultado = {}

        for url in urls:
            for param in payload:
                get_injection = requests.get(url, params= param)

                dicionario_resultado[url] = get_injection.status_code
        return dicionario_resultado

if __name__ == "__main__":
    engine = Engine('https://www.google.com.br/')
    print(engine.get_urls())
    print(engine.check_ssrf(engine.get_urls()))