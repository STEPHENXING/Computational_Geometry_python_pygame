import pygame
import random

# 定义点(Point)结构体
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 定义三角形(Triangle)结构体
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    # 计算两点向量的叉积
    def cross_product(self, p1, p2, p3):
        return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

    # 判断点P是否在三角形内部
    def is_point_in_triangle(self, p):
        # 计算三个边与点p的叉积
        cross1 = self.cross_product(self.p1, self.p2, p)
        cross2 = self.cross_product(self.p2, self.p3, p)
        cross3 = self.cross_product(self.p3, self.p1, p)

        # 如果三个叉积符号相同，说明点在三角形内部或者在边上
        if (cross1 > 0 and cross2 > 0 and cross3 > 0) or (cross1 < 0 and cross2 < 0 and cross3 < 0):
            return True
        return False

# 初始化pygame
pygame.init()

# 设置窗口尺寸
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Point In Triangle Test')

# 设置三角形顶点（可以根据需要修改）
p1 = Point(150, 100)
p2 = Point(450, 100)
p3 = Point(300, 450)
triangle = Triangle(p1, p2, p3)

# 画三角形
def draw_triangle():
    pygame.draw.polygon(screen, (255, 255, 255), [(p1.x, p1.y), (p2.x, p2.y), (p3.x, p3.y)], 2)

# 生成随机点
def generate_random_points(n):
    points = []
    for _ in range(n):
        x = random.randint(0, width)
        y = random.randint(0, height)
        points.append(Point(x, y))
    return points

# 主循环
running = True
random_points = generate_random_points(100)  # 生成100个随机点

while running:
    screen.fill((0, 0, 0))  # 填充背景为黑色
    draw_triangle()  # 画三角形

    # 绘制每个点并判断是否在三角形内
    for p in random_points:
        if triangle.is_point_in_triangle(p):
            pygame.draw.circle(screen, (0, 255, 0), (p.x, p.y), 5)  # 绿色表示在三角形内
        else:
            pygame.draw.circle(screen, (255, 0, 0), (p.x, p.y), 5)  # 红色表示不在三角形内

    pygame.display.flip()  # 刷新显示

    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
