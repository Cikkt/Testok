# -*- coding:utf8 -*-
import pytest
import allure


class Test001(object):
    @staticmethod
    def setup_class():
        print('========开始========')

    @staticmethod
    def teardown_class():
        print('========结束========')

    def test_001(self):
        allure.attach('瞎ffの测试用例')
        print('test001')

    @allure.severity('BLOCKER')
    @pytest.mark.skipif(3 > 1, reason='计算错误')
    def test_002(self):
        print('test002')

    @pytest.mark.skipif(4 > 3, reason='错了')
    def test_003(self):
        allure.attach('哈哈哈哈哈')


if __name__ == '__main__':
    pytest.main()
