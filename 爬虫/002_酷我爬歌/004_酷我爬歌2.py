from os import mkdir
from sys import exit
import requests
from tkinter import Frame, Label, Button, Entry


class DownloadMp3():
    def __init__(self, musicName):
        self.headers = {'Referer': 'http://www.kuwo.cn/search/list?key=',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
                        'csrf': 'NZNCXJFZLFF',
                        'Host': 'www.kuwo.cn',
                        'Cookie': '_ga=GA1.2.172942019.1580702894; _gid=GA1.2.771718281.1580890479; uname3=%u3081%u3044%u305F%u3093%u3066%u3044%u3053%u306A%u3093; t3kwid=235511292; userid=235511292; websid=2033651825; pic3="http://q.qlogo.cn/qqapp/100243533/BEB10B9B72AB7C5E6700E08B820BA1C5/100"; t3=qq; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1580702894,1580890479,1580891122; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1580892336; kw_token=NZNCXJFZLFF'
                        }
        self.musicName = musicName
        self.musicInfo = []
        self.__get_rid()
        self.musicUrl = []
        self.__git_url()

    def __get_rid(self):
        musicName = self.musicName
        url_params = {'key': musicName, 'pn': '1', 'rn': '30',
                      'reqId': '61bf6c51-4d57-11ea-893f-b927b601bf15'}
        url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord'

        response = requests.get(url, params=url_params,
                                headers=self.headers).json()
        for musicInfo in response['data']['list']:
            self.musicInfo.append((musicInfo['name'], musicInfo['rid']))

    def __git_url(self):
        for musicInfo in self.musicInfo:
            rid = musicInfo[1]
            url_params = {'format': 'mp3', 'rid': rid, 'response': 'url',
                          'type': 'convert_url3', 'br': '128kmp3', 'from': 'web',
                          't': '1581487410919', 'reqId': '64f38680-4d5d-11ea-b170-91f70fff34d4'}
            url = 'http://www.kuwo.cn/url'

            response = requests.get(
                url, params=url_params, headers=self.headers).json()
            self.musicUrl.append((musicInfo[0], response['url']))

    def Down(self):
        mkdir(self.musicName)
        for musicUrl in self.musicUrl:
            mp3 = requests.get(musicUrl[1]).content
            with open('%s/%s.mp3' % (self.musicName, musicUrl[0]), 'wb') as f:
                f.write(mp3)
        exit()


class createWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.__createModule()

    def __createModule(self):
        self.nameLabel = Label(self, text='请输入歌手名称')
        self.nameEntry = Entry(self, text='')
        self.quitButton = Button(self, text='下载', command=self.__download)
        self.nameLabel.pack()
        self.nameEntry.pack()
        self.quitButton.pack()

    def __download(self):
        musicName = self.nameEntry.get()
        mp3ins = DownloadMp3(musicName)
        mp3ins.Down()


if __name__ == '__main__':
    window = createWindow()
    window.master.title('歌曲下载')
    window.master.geometry('300x150')
    window.mainloop()
