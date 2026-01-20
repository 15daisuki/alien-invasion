import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True: # 游戏主循环
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self): # 处理事件（键盘 / 鼠标 / 退出）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 事件监听 用户请求关闭窗口的事件
                sys.exit()

            elif event.type == pygame.KEYDOWN: # 被按下的那一瞬间
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP: # 被松开 的那一瞬间
                self._check_keyup_events(event)
    def _check_keydown_events(self, event):
        # 响应按下
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True # 按住右键 → 飞机一直往右动
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True # 按住左键 → 飞机一直往左动
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        # 响应松开
        if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False # 松开右键 → 飞机立刻停
        elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False # 松开左键 → 飞机立刻停

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed: # 限制子弹数量
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹的位置并删除已消失的子弹"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if not self.aliens:      # 删除现有子弹并创建新的舰队
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2* alien_width

            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit!!!")

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) # 背景色
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip() # 刷新屏幕

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


             # FPS

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

# 13.6 结束游戏