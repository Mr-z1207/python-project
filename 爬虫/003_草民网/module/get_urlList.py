import requests
import parsel


class Reques():
    def __init__(self, url):
        self.url = url
        self.__get_response()

    def __get_response(self):
        response = requests.get(self.url)
        response.encoding = response.apparent_encoding
        self.response = response

    def get_content(self, cssRe):
        sel = parsel.Selector(self.response.text)
        urlList = sel.css(cssRe).getall()
        return urlList


if __name__ == '__main__':
    caomin = Reques('https://www.cmdy5.com/')
    urlList = caomin.get_content(".nav-down-1[id^='topnav'] a::attr('href')")

    print(urlList)
