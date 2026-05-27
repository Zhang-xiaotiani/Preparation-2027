# -*- coding: utf-8 -*-
"""
题目: NeetCode lc_003_arrays_Two_Sum : Two Sum
难度: Easy
首次创建日期: 2026/5/27
最后复习日期: 2026/5/27
链接: https://neetcode.io/problems/two-integer-sum/question?list=neetcode150

核心思路:
    使用 map 來存儲 nums 中 key 和 value 的關係，在遍历数组时同时检查 map 中是否存在 target-nums[i] ，若存在，则代表已经找到最小的 index

复杂度:
    时间复杂度: O(N)
    空间复杂度: O(N)

易错坑点/重刷提示:
    1. 不能对 nums 排序
"""
from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict()
        for i,item in enumerate(nums):
            if (target - item) in d:
                return [d[target - item], i]
            d[item] = i
      

s= Solution()
print(s.twoSum([3,2,3],5))