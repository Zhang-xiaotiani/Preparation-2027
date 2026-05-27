# -*- coding: utf-8 -*-
"""
题目: NeetCode lc_004_arrays_Group_Anagrams : groupAnagrams
难度: Medium
首次创建日期: 2026/5/27
最后复习日期: 2026/5/27
链接: https://neetcode.io/problems/anagram-groups/question?list=neetcode150

核心思路:
    1. SolutionSort 直接使用 str.sort 排序作为 dict 的唯一键
    2. sort 有时间消耗，可以使用26位长度的数组来标记某个字母出现的次数，最终将该数组转换位唯一的键。（题目说明只有小写字母组成）

复杂度:
    时间复杂度: O(N)
    空间复杂度: O(1)

易错坑点/重刷提示:
    1. 当使用字符频率数组作为字典键时，必须将其转换为不可变类型（例如 Python 中的元组或其他语言中的字符串）。列表和数组是可变的，不能直接用作字典键。
    2. 将频数转换为字符串时，使用简单的字符串拼接（不带分隔符）可能会导致冲突。例如，频数 [1,11] 和 [11,1] 都可能生成相同的字符串“111”。
"""
from collections import Counter, defaultdict
from typing import List


# 排序
class SolutionSort:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c = defaultdict(list)
        for item in strs:
            c["".join(sorted(item))].append(item)
        return list(c.values())


# 26位字母数组
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c = defaultdict(list)
        for item in strs:
            a = [0] * 26
            for i in item:
                a[ord(i) - ord('a')] += 1
            c[tuple(a)].append(item)
        return list(c.values())


s = Solution()
print(s.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
