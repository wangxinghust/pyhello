import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试name_function.py"""
    
    # 方法名必须以test打头
    def test_fist_last_name(self):
        """能够正确的处理像Janis Joplin这样的名字吗？"""
        formatted_name=get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
    def test_first_midlle_last_name(self):
        """能够正确处理像 Wolfgang Amadeus Mozart 这样的名字马？"""
        formatted_name=get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,"Wolfgang Amadeus Mozart")
unittest.main()