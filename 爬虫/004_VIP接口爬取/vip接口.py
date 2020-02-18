import re
import requests
import webbrowser as web
import tkinter as tk
from tkinter import ttk

url = 'http://qmaile.com/'                                     # vip解析网站
req = requests.get(url)                                        # 获取网站

req.encoding = req.apparent_encoding                           # 自动匹配正确的编码

regular = re.compile('<option value="(.*?)" selected="">')     # 定义正则规则
"""
从compile()函数的定义中，可以看出返回的是一个匹配对象
compile()与findall()一起使用，返回一个列表。

网站格式：
<option value="http://jx.du2.cc/?url=" selected="">⑤号通用vip引擎系统【全网解析】</option>

.*具有贪婪的性质，首先匹配到不能匹配为止，根据后面的正则表达式，会进行回溯。
.*？则相反，一个匹配以后，就往下进行，所以不会进行回溯，具有最小匹配的性质。
？表示非贪婪模式，即为匹配最近字符 如果不加?就是贪婪模式a.*bc 可以匹配  abcbcbc
"""

result = re.findall(regular, req.text)               # 在网站内容中按规则查找，返回解析链接列表


def play():
    web.open(result[value1.current()] + value2.get())


window = tk.Tk()                                     # 创建窗口对象
window.geometry('400x200')                           # 设置窗口大小
window.title('VIP解析')                              # 设置窗口标题

# 设置上边frame框架控件；在屏幕上显示一个矩形区域，多用来作为容器
# 用来放两个标签，下拉框和输入框
ContentBoxTop = tk.Frame(window, width=200)
ContentBoxTop.pack(side=tk.TOP, anchor='s')

# 设置下边frame框架控件；在屏幕上显示一个矩形区域，多用来作为容器
# 用来放按钮
ContentBoxBottom = tk.Frame(window, width=200)
ContentBoxBottom.pack(side=tk.TOP, anchor='n', fill='y',
                      expand='yes')

# 设置左边frame框架控件；在屏幕上显示一个矩形区域，多用来作为容器
# 用来放两个标签控件
ContentBoxTopLeft = tk.Frame(ContentBoxTop, width=200)
ContentBoxTopLeft.pack(side=tk.LEFT, anchor='n', fill='x',
                       expand='yes', pady='30', padx='15')

# 设置右边frame框架控件；在屏幕上显示一个矩形区域，多用来作为容器
# 用来放下拉框和输入框
ContentBoxTopRight = tk.Frame(ContentBoxTop, width=200)
ContentBoxTopRight.pack(side=tk.RIGHT, anchor='n', fill='x',
                        expand='yes', pady='30', padx='15')

txt1 = tk.Label(ContentBoxTopLeft, text='选择接口：')       # 设置标签框
txt1.pack(side=tk.TOP, anchor='e', pady='5')

value1 = ttk.Combobox(ContentBoxTopRight, width=100)       # 设置下拉框
value1['value'] = ['①号通用vip引擎系统【稳定通用】',
                   '②号通用vip引擎系统【稳定通用】',
                   '③号通用vip引擎系统【稳定通用】',
                   '④号通用vip引擎系统【稳定通用】',
                   '⑤号通用vip引擎系统【全网解析】']
value1.current(0)
value1.pack(side=tk.TOP, anchor='w', pady='5')

txt2 = tk.Label(ContentBoxTopLeft, text='视频地址：')       # 设置标签框
txt2.pack(side=tk.TOP, anchor='e', pady='5')

value2 = tk.Entry(ContentBoxTopRight, text='', width=103)  # 设置输入框
value2.pack(side=tk.TOP, anchor='w', pady='5')

button = tk.Button(ContentBoxBottom, text='开始播放', font=12, command=play)  # 设置按钮
button.pack(side=tk.TOP, anchor='center')

window.mainloop()
