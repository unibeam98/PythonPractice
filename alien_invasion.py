import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # 初始化pygame
    pygame.init()

    # 初始化游戏屏幕、游戏名设置，屏幕大小设置时要加括号
    ai_settings = Settings()  # 初始设置类的实例化
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船、一个子弹编组和一个外星人组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, aliens, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, screen, ship, aliens, bullets)

        # 填充屏幕背景，飞机，并进行刷新
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


if __name__ == '__main__':
    run_game()
