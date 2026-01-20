class Settings:        #  储存游戏中所有设置的类
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5

        self.bullet_speed = 4
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (57, 197, 187)
        self.bullets_allowed = 10

        self.alien_speed = 1.0
        self.fleet_drop_speed = 100
        self.fleet_direction = 1 # 向右移动 -1为向左

