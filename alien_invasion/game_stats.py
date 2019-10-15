"""
用于跟踪游戏统计信息
"""


class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        # 让游戏一开始处于非活动状态
        self.game_active = False
        self.ai_settings = ai_settings

        # 最高分设置，无需重置，写在json文件里更好，每次打开游戏后，最高分依然会被重置
        self.high_score = 0

        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
