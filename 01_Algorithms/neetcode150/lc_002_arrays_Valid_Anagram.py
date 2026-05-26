# -*- coding: utf-8 -*-
"""
题目: NeetCode lc_002_arrays_Valid_Anagram : Valid Anagram
难度: Easy
首次创建日期: 2026/5/26
最后复习日期: 2026/5/26
链接: https://neetcode.io/problems/is-anagram/question?list=neetcode150

核心思路:
    空间换时间，定义两个 map 分别存储 s 和 t

复杂度:
    时间复杂度: O(N)
    空间复杂度: O(N+M) 最低O(1)

易错坑点/重刷提示:
    1. 原生 dict 的 update 底层逻辑是用来合并两个字典的。你每遍历一个字符，它都会在内存里凭空创建一个新的临时字典 {s[i]: ...}，然后再调用 update 方法把它融合进原字典。
    2. default dict 当key不存在时，返回1，而不是报错
    3. counter 是 dict 的计数字典，专门用来统计元素出现次数
"""
from collections import defaultdict, Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap_s = {}
        hashmap_t = {}
        for i in range(len(s)):
            s_i_count = hashmap_s.get(s[i], 0)
            t_i_count = hashmap_t.get(t[i], 0)
            hashmap_s.update({
                s[i]: s_i_count + 1
            })
            hashmap_t.update({
                t[i]: t_i_count + 1
            })
        return hashmap_s == hashmap_t


class Solution_defaultdict:
    # 空间换时间
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = defaultdict(int), defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(t)):
            d1[s[i]] += 1
            d2[t[i]] += 1
        return d1 == d2

class Solution_counter:
    # 空间换时间
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


class Solution_sort:
    # 空间复杂度O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)