class Settings():
    """存储《外星人入侵》的所有初始设置的参数"""
    def __init__(self):
        """初始化游戏的设置"""
        '''初始化游戏的静态设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 设置飞船
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_speed_factor = 3
        # 屏幕上可以同时出现多少颗子弹
        self.bullets_allowed = 6

        # 外星人设置
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 15
        # 外星人移动方向
        self.fleet_direction = 1
