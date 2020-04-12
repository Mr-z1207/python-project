import os

os.chdir('C:/Users/14360/Desktop/test')

L_fileNames = os.listdir()

n = 0
for i in L_fileNames:
    os.rename(i, f'2021考研数学张宇基础30讲_{n:03}.pdf')
    n = n + 1
