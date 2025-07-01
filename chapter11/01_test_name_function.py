# 测试函数
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase): # 这个类必须继承unittest.TestCase类
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗?"""
        formatted_name = get_formatted_name(first='janis',middle='',last='joplin')
        self.assertEqual(formatted_name,'Janis Joplin') # 一个断言方法。断言方法用来核实得到的结果是否与期望的结果一致

    def test_first_last_middle_name(self):
        """能够正确地处理像 Wolfgang Amadeus Mozart 这样的姓名吗?"""
        formatted_name = get_formatted_name('Wolfgang','Amadeus','Mozart')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart') 

# 代码行unittest.main()让Python运行这个文件中的测试
unittest.main()