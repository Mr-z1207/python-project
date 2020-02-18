import re
import os

import requests

url = 'https://pvp.qq.com/web201605/js/herolist.json'

heroList = requests.get(url).json()


def getSkinName(heroInof):
    skinName_list = []
    if 'skin_name' in heroInof:
        skinName_list = re.split(r'\|', heroInof['skin_name'])
        if heroInof['title'] in skinName_list:
            pass
        else:
            skinName_list.insert(0, heroInof['title'])
    else:
        skinName_list.insert(0, heroInof['title'])
    return skinName_list


def dow_img(heroList):
    for heroInof in heroList:
        os.mkdir('C:/Users/14360/Desktop/王者原画/%s' % heroInof['cname'])
        os.chdir('C:/Users/14360/Desktop/王者原画/%s' % heroInof['cname'])
        skinName_list = getSkinName(heroInof)
        _len = len(skinName_list)
        for v in range(_len):
            img = requests.get('https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/%s/%s-bigskin-%s.jpg' % (heroInof['ename'], heroInof['ename'], v+1))
            with open('%s.jpg' % skinName_list[v], 'wb') as file:
                file.write(img.content)


ishas = os.path.exists('C:/Users/14360/Desktop/王者原画')
if ishas:
    print('文件已存在，请删除‘C:/Users/14360/Desktop/王者原画’再试')
else:
    os.mkdir('C:/Users/14360/Desktop/王者原画')
    dow_img(heroList)
