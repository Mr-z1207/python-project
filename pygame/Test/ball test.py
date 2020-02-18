import pygame
import sys

pygame.init()  # 初始化pygame;   # 有初始就要有退出
size = width, height = 320, 550  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口;   # 返回了一个屏幕Surface对象

# 设置参数
color = (255, 255, 255)  # 设置颜色
speed = [5, 5]

ball = pygame.image.load('./img/ball.png')  # 加载图片

ballrect = ball.get_rect()  # 获取矩形图片区域(0, 0, 111, 111)(left, top, width, height)

# 限制移动速度 创建一个Clock对象
# 使用pygame时钟之前，必须先创建Clock对象的一个实例，然后在while循环中设置多长时间运行一次。
clock = pygame.time.Clock()

while True:  # 死循环-保持窗口持续显示
    clock.tick(60)  # 每秒执行60次循环
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()

    screen.fill(color)  # 填充颜色(设置为0，执不执行这行代码都一样)
    screen.blit(ball, ballrect)  # 将图片画到窗口上(参数：要画的图片,和画的位置)

    ballrect = ballrect.move(speed)  # 设置位置移动
    # 碰撞检测
    # 碰到左右边缘
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    # 碰到上下边缘
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    pygame.display.flip()  # 更新全部显示


pygame.quit()  # 退出pygame
