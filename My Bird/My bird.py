from sys import exit
from random import randint

import pygame


class Bird(object):                                    # 定义一个鸟类
    def __init__(self):
        """ 定义初始属性 """
        self.birdRect = pygame.Rect(65, 50, 50, 50)    # 鸟的默认矩形 (left, top, width, height)
        # 定义鸟的3种状态列表
        self.birdStatus = [pygame.image.load("./img/bird/1.png"),
                           pygame.image.load("./img/bird/2.png"),
                           pygame.image.load("./img/bird/dead.png")]
        self.status = 0                                # 默认飞行状态
        self.birdX = 120                               # 鸟所在X轴坐标,即是向右飞行的速度
        self.birdY = 350                               # 鸟所在Y轴坐标,即上下飞行高度
        self.speed = 0                                 # 默认速度
        self.dead = False                              # 默认小鸟生命状态为活着

    def birdUpdate(self):
        """ 定义鸟的状态更新 """
        self.speed -= 1                                # 速度递减，上升越来越慢
        self.birdY -= self.speed                       # 鸟Y轴坐标减小，小鸟上升
        if self.speed < 5:
            self.status = 0

        self.birdRect[1] = self.birdY                  # 修改鸟的矩形Top值


class Pipeline(object):                                # 定义一个管道
    def __init__(self):
        """ 定义初始属性 """
        self.Pipex = 400                               # 管道所在X轴坐标
        self.Pipey = 300                               # 管道所在y轴坐标
        self.RePipey = True                            # 是否随机生成Y轴坐标
        # 导入上下两根管子的图片
        self.TopPipe = pygame.image.load('./img/Pipeline/top.png')
        self.BottomPipe = pygame.image.load('./img/Pipeline/bottom.png')

    def updatePipeline(self):
        """ 定义水平移动 """
        self.Pipex -= 5                                # 向左移动速度


def createMap():
    """定义创建地图的方法"""
    screen.fill((255, 255, 255))                               # 填充颜色
    screen.blit(background, (0, 0))                            # 填入到背景

    # 显示管道
    if Pipeline.RePipey:
        Pipeline.Pipey = randint(1, 450)
        Pipeline.RePipey = False
    screen.blit(Pipeline.TopPipe, (Pipeline.Pipex, -Pipeline.Pipey))
    screen.blit(Pipeline.BottomPipe, (Pipeline.Pipex, 490 - Pipeline.Pipey + 150))
    Pipeline.updatePipeline()
    if Pipeline.Pipex < -80:
        Pipeline.Pipex = 400
        Pipeline.RePipey = True

    # 显示小鸟
    screen.blit(Bird.birdStatus[Bird.status], Bird.birdRect)   # 设置小鸟的坐标
    Bird.birdUpdate()                                          # 鸟移动

    pygame.display.update()                                    # 更新显示


if __name__ == '__main__':
    pygame.init()                              # 初始化pygame;
    size = width, height = 400, 650            # 设置窗口大小;
    screen = pygame.display.set_mode(size)     # 显示窗口;

    clock = pygame.time.Clock()                # 创建时钟实例
    Pipeline = Pipeline()                      # 创建管道实例
    Bird = Bird()                              # 创建鸟的实例

    background = pygame.image.load("./img/background/background.png")  # 加载背景图片

    while True:                                # 死循环-保持窗口持续显示
        clock.tick(60)                         # 每秒执行60次
        for event in pygame.event.get():       # 遍历事件
            if event.type == pygame.QUIT:      # 如果检测到事件是关闭窗口,就关闭
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not Bird.dead:
                Bird.status = 1
                Bird.speed = 10                # 改变速度

        createMap()                            # 生成地图
