import pygame
class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp') # 读取图片
        self.image = pygame.transform.scale(self.image, (60,80)) # 改大小
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom # 位置
        self.moving_right = False # 不动
        self.moving_left = False # 不动

    def update(self):
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
    def blitme(self):
        self.screen.blit(self.image, self.rect)