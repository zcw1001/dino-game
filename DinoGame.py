import pygame as pg
from random import randrange
from sys import exit
from collections import deque

from Config import *
from Dinosaur import Dinosaur
from Track import Track
from Score import Score
from Obstacle import SmallCactus, LargeCactus, Pteranodon


class DinoGame:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.dinosaur = Dinosaur()
        self.track = Track()
        self.score = Score()
        self.obstacles = deque()
        self.last_obstacle = -1
        self.n_delete = 0 # 需要删除多少个障碍
        self.speed = 60

    def _generate_obstacles(self):
        if not len(self.obstacles) or (len(self.obstacles) == 1 and 0 < self.obstacles[-1].img_rect.x < WIDTH // 3):
            i = randrange(0, 3)
            while i == self.last_obstacle:
                i = randrange(0, 3)
            self.last_obstacle = i
            if i == 0:
                self.obstacles.append(SmallCactus())
            elif i == 1:
                self.obstacles.append(LargeCactus())
            else:
                self.obstacles.append(Pteranodon())

    def _draw_obstacles(self):
        def deleteObstacle():
            self.n_delete += 1
        def collide(A, B):
            x_collide = B.img_rect.x + B.img_rect.w * 0.5 <= A.img_rect.x + A.img_rect.w <= B.img_rect.x + B.img_rect.w + A.img_rect.w
            y_collide = B.img_rect.y + B.img_rect.h * 0.5 <= A.img_rect.y + A.img_rect.h <= B.img_rect.y + B.img_rect.h + A.img_rect.h
            return x_collide and y_collide
        for obstacle in self.obstacles:
            obstacle.draw(self.window, self.speed, deleteObstacle)
            if collide(self.dinosaur, obstacle):
                # pg.draw.rect(self.window, (255, 0, 0), obstacle.img_rect, 2)
                # pg.draw.rect(self.window, (255, 255, 0), self.dinosaur.img_rect, 2)
                pg.time.delay(1000)
                pg.quit()
                exit()
        for _ in range(self.n_delete):
            self.obstacles.popleft()
        self.n_delete = 0

    def draw(self):
        # 显示跑道
        self.track.draw(self.window, self.speed)
        # 显示恐龙
        self.dinosaur.draw(self.window)
        # 生成障碍
        self._generate_obstacles()
        self._draw_obstacles()
        # 显示分数
        self.score.draw(self.window)

        self.clock.tick(120)
        pg.display.flip()

    def start(self):
        while True:
            self.window.fill(WHITE)
            self.window.convert()
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()
                    exit()

            # 检测按键输入
            pressed = pg.key.get_pressed()
            self.dinosaur.update(pressed)

            # 增加得分
            def incrementSpeed():
                self.speed += 1
            self.score.increment(incrementSpeed)

            # 画图
            self.draw()
        

if __name__ == '__main__':
    game = DinoGame()
    game.start()