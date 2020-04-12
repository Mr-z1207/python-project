from aip import AipSpeech
import time
import pygame
import py

""" 你的百度 APPID AK SK
https://console.bce.baidu.com/ai/#/ai/speech/app/list       应用列表
http://ai.baidu.com/docs#/TTS-Online-Python-SDK/top         API

https://ai.baidu.com/aidemo?type=tns2&idx=1&tex=你好&cuid=baidu_speech_demo&cod=2&lan=zh&ctp=1&pdt=1&spd=5&per=2&vol=1&pit=5

返回wav格式 后面的参数 支持 音量 男女调整  自己那去玩
"""
APP_ID = '14709562'
API_KEY = 'nLTx7voQrNsMlm2e56TdPnTr'
SECRET_KEY = 'wsbf0KSTNUBApskLNFDv4Zt8E3R3XAne'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# text111 = "春江潮水连海平 海上明月若潮升。黄鹤楼，两只黄鹤鸣翠鸟，我却还是单身狗"
text111 = input("请输入要转换的文字：")
result = client.synthesis(text111, 'zh', 1, {
    'vol': 5,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open(r'C:\auido.mp3', 'wb') as f:
        f.write(result)

# ------------------------------------------------------

file = r'C:\auido.mp3'
pygame.mixer.init()
print("播放")
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()
time.sleep(10)
pygame.mixer.music.stop()
