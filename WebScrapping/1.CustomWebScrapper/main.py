import urllib.request
from bs4 import BeautifulSoup

class Scrapper:
    
    def __init__(self, url):
        self.url = url
        self.soup = None

    def scrape(self):
        r = urllib.request.urlopen(self.url)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            print(url)



if __name__ == "__main__":
    url = r"https://amanxai.com/2020/08/23/scraping-youtube-with-python/"
    scrapper = Scrapper(url)
    scrapper.scrape()