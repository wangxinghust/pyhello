"""
各种功能函数
"""

import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien


def check_events(ship, ai_settings, screen, bullets, stats, play_button, aliens, scoreboard):
    """响应鼠标和键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(play_button, mouse_x, mouse_y,
                              stats, ship, aliens, bullets, ai_settings, screen, scoreboard)


def check_play_button(play_button, mouse_x, mouse_y, stats, ship,
                      aliens, bullets, ai_settings, screen, scoreboard):
    """在玩家单击play按钮后开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    # 避免play按钮消失后，依旧可以点击响应区域并响应的问题
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌图像
        scoreboard.prep_level()
        scoreboard.prep_score()
        scoreboard.prep_high_score()
        scoreboard.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_keydown_events(event, ship, ai_settings, screen, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, ai_settings, screen, ship)
    # 结束游戏快捷键
    elif event.key == pygame.K_q:
        sys.exit(0)


def fire_bullet(bullets, ai_settings, screen, ship):
    """如果还没有到达限制，就发射一颗子弹"""
    if len(bullets) < ai_settings.bullet_allowed:
        # 创建一颗子弹，并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats, scoreboard):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕 fill Surface with a solid color
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重新绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 显示得分
    scoreboard.show_score()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见 Update the full display Surface to the screen
    pygame.display.flip()


def bullets_update(bullets, aliens, ai_settings, screen, ship, scoreboard, stats):
    """更新子弹的位置，并删除已经消失的子弹"""

    # 更新子弹位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():  # 在for循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 检查是否有子弹击中了外星人
    # 如果是这样，就删除相应的外星人和子弹
    # Find all sprites that collide between two groups.
    check_bullets_aliens_collisions(
        bullets, aliens, ai_settings, screen, ship, scoreboard, stats)


def check_bullets_aliens_collisions(bullets, aliens, ai_settings, screen, ship, scoreboard, stats):
    """响应子弹和外星人的碰撞"""

    # 检查是否有子弹击中了外星人
    # 如果是这样，就删除相应的外星人和子弹
    # Find all sprites that collide between two groups.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += len(aliens)*ai_settings.alien_points
            scoreboard.prep_score()
        check_high_score(stats, scoreboard)

    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人,并加快游戏节奏
        bullets.empty()
        ai_settings.increase_speed()

        # 提高等级
        stats.level += 1
        scoreboard.prep_level()

        create_fleet(ai_settings, screen, aliens, ship)


def create_fleet(ai_settings, screen, aliens, ship):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可以容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_aliens_y(
        ai_settings, ship.rect.height, alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        # 创建第一行外星人
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, alien_number, row_number, aliens)


def create_alien(ai_settings, screen, alien_number, row_number, aliens):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width+2*alien_number*alien_width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height+2*alien.rect.height*row_number

    aliens.add(alien)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可以容纳多少个外星人"""
    available_space_x = ai_settings.screen_width-2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x


def get_number_aliens_y(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height -
                         (3*alien_height)-ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows


def update_aliens(ai_settings, aliens, ship, stats, screen, bullets, scoreboard):
    """
    检查是否有外星人位于屏幕边缘
    更新外星人的位置
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检查外星人和飞船之间的碰撞
    # Simple test if a sprite intersects anything in a group.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(stats, bullets, aliens, ai_settings, screen, ship, scoreboard)

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(screen, aliens, stats, bullets,
                        ai_settings, ship, scoreboard)


def check_aliens_bottom(screen, aliens, stats, bullets, ai_settings, ship, scoreboard):
    """ 检查是否有外星人到达屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样处理
            ship_hit(stats, bullets, aliens, ai_settings,
                     screen, ship, scoreboard)
            break


def ship_hit(stats, bullets, aliens, ai_settings, screen, ship, scoreboard):
    """响应被外星人撞到的飞船"""
    if stats.ship_left > 0:

        stats.ship_left -= 1
        # 更新记分牌
        scoreboard.prep_ships()

        # 清空外星人和子弹列表
        bullets.empty()
        aliens.empty()

        # 创建一群新的外星人，并将其飞船放至屏幕底端中央
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_high_score(stats, scoreboard):
    """检查是否诞生了最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()
