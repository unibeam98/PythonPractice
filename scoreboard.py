import pygame.font
from  pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """显示得分信息"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        # 显示得分信息的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始得分图像和最高得分的图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将得分转化为图形"""
        # 得分圆整
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 放置在屏幕右上角
        self.screen_rect = self.score_image.get_rect()
        self.screen_rect.right = self.ai_settings.screen_width - 20
        self.screen_rect.top = 20

    def prep_high_score(self):
        """将最高得分转化为图像"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.ai_settings.bg_color)

        # 将最高的分防止在屏幕顶端
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = int(self.ai_settings.screen_width / 2)
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """将等级转化为图像"""
        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.text_color, self.ai_settings.bg_color)
        # 将得分放在得分下方
        self.leve_rect = self.level_image.get_rect()
        self.leve_rect.right = self.screen_rect.right
        self.leve_rect.top = self.screen_rect.bottom + 10

    def prep_ships(self):
        """显示还剩下多少飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 20
            self.ships.add(ship)

    def show_score(self):
        """显示得分"""
        self.screen.blit(self.score_image, self.screen_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.leve_rect)
        self.ships.draw(self.screen)