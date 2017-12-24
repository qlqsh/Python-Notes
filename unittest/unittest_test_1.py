#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

# 标准单元测试
class TestAddition(unittest.TestCase):
    def setUp(self):
        """每个测试的开始都会运行一次"""
        print("设置测试---")
    
    def tearDown(self):
        """每个测试的结束都会运行一次"""
        print("结束测试---")
    
    def test_twoPlusTwo(self):
        total = 2+2
        self.assertEqual(4, total)

if __name__ == '__main__':
    unittest.main()