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

    def test_003(self):
        print('test6')


if __name__ == '__main__':
    pytest.main()
