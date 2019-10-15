"""
主程序
"""

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_function as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建外星人群组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, aliens, ship)
    # 创建一个用于存储游戏统计信息的实例，并创建计分牌
    stats = GameStats(ai_settings)
    scoreborad = Scoreboard(ai_settings, screen, stats)
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship, ai_settings, screen, bullets,
                        stats, play_button, aliens, scoreborad)

        if stats.game_active:
            # 更新飞船、外星人和未消失子弹的位置
            ship.update()
            gf.bullets_update(bullets, aliens, ai_settings,
                              screen, ship, scoreborad, stats)
            gf.update_aliens(ai_settings, aliens, ship, stats,
                             screen, bullets, scoreborad)

        # 重新绘制屏幕
        gf.update_screen(ai_settings, screen, ship,
                         bullets, aliens, play_button, stats, scoreborad)


run_game()
