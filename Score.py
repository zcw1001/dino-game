import pygame as pg

class Score:
    def __init__(self):
        self.points = 0
        self.cooldown = 12
        self.cooldown_cnt = 0

    def increment(self, callback):
        if self.cooldown_cnt == 0:
            self.points += 1
            self.cooldown_cnt += 1
        elif self.cooldown_cnt == self.cooldown:
            self.cooldown_cnt = 0
        else:
            self.cooldown_cnt += 1

        if self.points > 0 and self.points % 100 == 0:
            callback()

    def draw(self, window):
        font_file = pg.font.match_font("songti") 
        font = pg.font.Font(font_file, 30)
        text = font.render(f'得分: {self.points}', True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        window.blit(text, textRect)