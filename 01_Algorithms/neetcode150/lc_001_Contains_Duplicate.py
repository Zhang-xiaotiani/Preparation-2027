# -*- coding: utf-8 -*-
"""
题目: Contains Duplicate
难度: Easy
最后复习日期:  2026-5-26
链接: https://neetcode.io/problems/duplicate-integer/question?list=neetcode150

核心思路:
    利用 set 中元素的不可重复性

复杂度:
    时间复杂度: O(N) - 仅需遍历一次字符串。
    空间复杂度: O(N) - M 为字符集大小。

易错坑点/重刷提示:
    1. python中数组可直接转换为 set，无需便利
"""
from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_tmp = set(nums)
        return True if len(hash_tmp) < len(nums) else False
