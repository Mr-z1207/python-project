from sys import exit
from random import randint

import pygame


class Bird(object):                                    # 定义一个鸟类
    def __init__(self):
        """ 定义初始属性 """
        self.game_active = False                       # 默认游戏未开始
        self.birdRect = pygame.Rect(120, 350, 40, 29)  # 鸟的默认矩形 (left, top, width, height)
        # 定义鸟的3种状态列表
        self.birdStatus = [pygame.image.load("./img/bird/1.png"), pygame.image.load("./img/bird/2.png")]
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
        self.Pipex = -90                               # 管道初始X轴坐标
        # 导入上下两根管子的图片
        self.TopPipe = pygame.image.load('./img/Pipeline/top.png')
        self.BottomPipe = pygame.image.load('./img/Pipeline/bottom.png')
        # 获取两个管子的矩形
        self.TopPopeRect = pygame.Rect(-98, 0, 98, 495)
        self.BottomPipeRect = pygame.Rect(-98, 0, 94, 499)

    def updatePipeline(self):
        """ 定义管子位置 """
        self.Pipex -= 5                                        # 向左移动速度
        self.TopPopeRect[0] = self.Pipex                       # 修改上管道left矩形值
        self.BottomPipeRect[0] = self.Pipex                    # 修改下管道left矩形值

        if self.Pipex < -98:                                   # 管道彻底移出屏幕左侧

            global score
            score += 1

            self.Pipex = 400                                   # 重置管道x坐标回右侧
            Pipey = randint(1, 450)                            # 随机生成一个高度
            self.TopPopeRect[1] = -Pipey                       # 改变管道top矩形值
            self.BottomPipeRect[1] = 490 - Pipey + 150


def checkDead():
    # 死亡判定
    """
    判断两个矩形是否相交
    flag = pygame.Rect.colliderect(rect1, rect2)
    相交返回True 否则返回 Fales
    存在另一种写法 rect2.colliderect(rect1)
    """
    # 鸟与上下管道碰撞
    if Pipeline.TopPopeRect.colliderect(Bird.birdRect) or Pipeline.BottomPipeRect.colliderect(Bird.birdRect):
        Bird.dead = True
        Bird.status = 2
        return True
    # 鸟飞出上下边界
    elif not 0 < Bird.birdRect[1] < height:
        Bird.dead = True
        Bird.status = 2
        return True
    else:
        return False


def getResutl():
    final_text1 = "Game Over"                                  # 设置结束文字
    final_text2 = "Your final score is:" + str(score)          # 设置结束文字（得分）

    ft1_surf = font.render(final_text1, 1, (242, 3, 36))       # 创建文字surf对象
    ft2_surf = font.render(final_text2, 1, (253, 177, 6))

    # 将文字画到屏幕上
    screen.blit(ft1_surf, [screen.get_width() / 2 - ft1_surf.get_width() / 2, screen.get_height() / 2 - ft1_surf.get_height() / 2 + 50])
    screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, screen.get_height() / 2 - ft2_surf.get_height() / 2 - 50])

    pygame.display.flip()                                     # 更新显示


def createMap():
    """定义创建地图的方法"""
    screen.fill((255, 255, 255))                               # 填充颜色
    screen.blit(background, (0, 0))                            # 填入到背景

    # 显示管道
    screen.blit(Pipeline.TopPipe, Pipeline.TopPopeRect)        # 画出两个管子
    screen.blit(Pipeline.BottomPipe, Pipeline.BottomPipeRect)

    # 显示小鸟
    screen.blit(Bird.birdStatus[Bird.status], Bird.birdRect)   # 设置小鸟的坐标

    # 开始游戏
    if Bird.game_active:
        Bird.birdUpdate()                                      # 鸟移动
        Pipeline.updatePipeline()                              # 管子移动
        # 显示分数
        score_surf = font.render('Score:' + str(score), -1, (255, 255, 255))
        screen.blit(score_surf, [screen.get_width() / 2 - score_surf.get_width() / 2, 50])

    pygame.display.update()                                    # 更新显示


if __name__ == '__main__':
    pygame.init()                              # 初始化pygame;
    size = width, height = 400, 650            # 设置窗口大小;
    pygame.display.set_caption('My Bird')      # 设置窗口标题;
    screen = pygame.display.set_mode(size)     # 显示窗口;

    pygame.font.init()                         # 初始化字体
    font = pygame.font.SysFont("Arial", 50)    # 设置字体和大小

    clock = pygame.time.Clock()                # 创建时钟实例
    Pipeline = Pipeline()                      # 创建管道实例
    Bird = Bird()                              # 创建鸟的实例

    score = -1                                  # 初始分数为-1

    background = pygame.image.load("./img/background/background.png")   # 加载背景图片

    while True:                                # 死循环-保持窗口持续显示
        clock.tick(60)                         # 每秒执行60次
        for event in pygame.event.get():       # 遍历事件
            if event.type == pygame.QUIT:      # 如果检测到事件是关闭窗口,就关闭
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not Bird.dead:  # 当鼠标点击，并且鸟没死
                if not Bird.game_active:       # 如果游戏未开始
                    Bird.game_active = True    # 改变游戏状态为开始
                Bird.status = 1                # 改变鸟的状态，更改图片
                Bird.speed = 12                # 改变速度

        if checkDead():
            getResutl()                        # 游戏结束，显示得分
        else:
            createMap()                        # 生成地图
