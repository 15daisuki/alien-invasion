import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)

    def run_game(self):
        while True: # 游戏主循环
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
    def _check_events(self): # 处理事件（键盘 / 鼠标 / 退出）
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 事件监听
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True # 按住右键 → 飞机一直往右动
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True # 按住左键 → 飞机一直往左动

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False # 松开右键 → 飞机立刻停
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False # 松开左键 → 飞机立刻停
    def _update_screen(self):
            self.screen.fill(self.settings.bg_color) # 背景色
            self.ship.blitme()
            pygame.display.flip() # 刷新屏幕
             # FPS

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


