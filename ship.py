import pygame
class Ship:
    def __init__(self, ai_game):
        # 初始化飞船并设置位置
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp') # 读取图片
        self.image = pygame.transform.scale(self.image, (60,80)) # 改大小

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom # 位置
        self.x = float(self.rect.x)

        self.moving_right = False # 不动
        self.moving_left = False # 不动

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
    def blitme(self):
        self.screen.blit(self.image, self.rect)