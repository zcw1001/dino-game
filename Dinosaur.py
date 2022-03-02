import pygame as pg
import os

class Dinosaur:
    def __init__(self):
        self.x = 80
        self.y = 310
        self.speed = 15
        
        self.RUNNING = [pg.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pg.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
        self.JUMPING = pg.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
        self.DUCKING = [pg.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pg.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]
        self.state = [True, False, False] # Running, Jumping, Ducking
        self.state_index = [0, 0, 0] # Running, Jumping, Ducking
        self.img = self.RUNNING[0] # Current image of the dinosaur
        self.img_rect = self.img.get_rect()
        self.img_rect.x = self.x
        self.img_rect.y = self.y
    
    def draw(self, window):
        window.blit(self.img, (self.img_rect.x, self.img_rect.y))

    def update(self, pressed):
        if self.state[0]: self.run()
        elif self.state[1]: self.jump()
        elif self.state[2]: self.duck()

        if not self.state[1] and pressed[pg.K_UP]: self.state = [False, True, False]
        elif not self.state[1] and pressed[pg.K_DOWN]: self.state = [False, False, True]
        elif not self.state[1] and not pressed[pg.K_DOWN]: self.state = [True, False, False]
    
    def run(self):
        self.img = self.RUNNING[(self.state_index[0] // 20) % 2]
        self.img_rect = self.img.get_rect()
        self.img_rect.x = self.x
        self.img_rect.y = self.y
        self.state_index[0] += 1

    def jump(self):
        self.img = self.JUMPING
        if self.state[1]:
            self.img_rect.y -= self.speed
            self.speed -= 0.5
            if self.speed < -15:
                self.speed = 15
                self.state = [True, False, False]

    def duck(self):
        self.img = self.DUCKING[(self.state_index[2] // 20) % 2]
        self.img_rect = self.img.get_rect()
        self.img_rect.x = self.x
        self.img_rect.y = self.y + 30
        self.state_index[2] += 1