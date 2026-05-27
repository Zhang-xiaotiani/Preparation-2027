# 🧩 NeetCode 150 滚动式刷题与防忘策略

> **核心原则：** 分类攻克为主，滚动复习为辅。绝不盲目乱刷，让做过的每一道题都变成肌肉记忆。

---

## 🔁 “抗遗忘”滚动复习机制 (Rolling Strategy)

为了彻底解决“刷到后面，前面忘光”的现象，严格执行 **"1 + 1" 日常模式**：

* **日常模式：**
  * **Step 1: 攻克新知识 (占 70% 时间)** -> 每天刷 1-2 道当前分类的新题，专注当前 Module，建立解题模版。
  * **Step 2: 滚动复习旧题 (占 30% 时间)** -> 每天从之前已通关的 Module 中随机抽取 1 道错题重刷。
* **周末清障：** 每周日为“固本培元日”，**不刷任何新题**。将本周做过的所有中等（Medium）难度题、以及之前卡壳的硬骨头，在不看题解的情况下盲写一遍。

---

## 📅 NeetCode 150 模块解锁路线图 (匹配 10 个月计划)

按照技术依赖关系，将 150 题拆分为四个核心梯队：

### 🧱 第一梯队：数据结构地基 (2026.06)
* **核心模块：** 1. `Arrays & Hashing` (数组与哈希 - 基础中的基础)
  2. `Two Pointers` (双指针 - 数组的衍生技巧)
  3. `Stack` (栈)
* **抗遗忘埋点：** 进入 `Two Pointers` 时，每天热身运动必须是一道 `Arrays` 的旧题。

### 🌀 第二梯队：线性与树状进阶 (2026.07)
* **核心模块：**
  1. `Sliding Window` (滑动窗口 - 滴滴限流、网络常考)
  2. `Binary Search` (二分查找)
  3. `Linked List` (链表 - 滴滴最爱手撕的结构，如反转、合并)
  4. `Trees` (二叉树 - 递归思维训练场)
* **抗遗忘埋点：** 刷 `Trees` 的期间，每周一、三、五必须随机抽一道 `Linked List` 或 `Sliding Window` 压惊。

### 🕸️ 第三梯队：高级结构与搜索 (2026.08 - 2026.09)
* **核心模块：**
  1. `Heap / Priority Queue` (堆与优先队列)
  2. `Backtracking` (回溯算法)
  3. `Graphs` & `Advanced Graphs` (图论 - 网约车地图/LBS核心算法底座)
  4. `Tries` (前缀树)

### 📈 第四梯队：大厂分水岭 (2026.10 - 2026.11)
* **核心模块：**
  1. `1-D Dynamic Programming` (一维动态规划)
  2. `2-D Dynamic Programming` (二维动态规划)
  3. `Greedy` (贪心算法)
  4. `Bit Manipulation` (位运算)

---

## 📝 Git 提交与笔记规范 (Code Logging Spec)

既然用了 Git 仓库，就要让它发挥最大复习效能。每次提交文件到 `01_Algorithms/LeetCode/` 时，严格遵循以下规范：

### 1. 文件命名
统一格式：`lc_[题号]_[英文下划线题目].py`
* 示例：`lc_0001_two_sum.py`

### 2. 代码头部模版 (重要：这是你的备忘录)
每个 Python 文件头部务必用多行注释包含以下三个要素：**核心思路**、**时空复杂度**、**易错坑点**。

```python
# -*- coding: utf-8 -*-
"""
题目: LeetCode 3. 无重复字符的最长子串 (Sliding Window 模块)
难度: Medium
最后复习日期: 2026-06-XX

核心思路:
    使用双指针维护一个滑动窗口 [left, right]。
    用哈希表(dict)记录每个字符最后出现的位置。
    当 right 指针遇到重复字符时，若该字符在窗口内，则将 left 移到该字符上次出现位置的下一位。

复杂度:
    时间复杂度: O(N) - 仅需遍历一次字符串。
    空间复杂度: O(min(N, M)) - M 为字符集大小。

易错坑点/重刷提示:
    1. left 指针更新时必须取 max(left, char_map[char] + 1)，防止 left 发生逆向倒退！
"""

def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}
    left = 0
    max_len = 0
    
    for right, char in enumerate(s):
        if char in char_map:
            # 坑点：防止 left 往左回跳
            left = max(left, char_map[char] + 1)
        char_map[char] = right
        max_len = max(max_len, right - left + 1)
        
    return max_len

🏆 通关标记机制 (全部通过后在此打勾 ☕)
当你在不看答案的情况下，把一个分类在 3天内滚动重刷全部通过，即可在下面打勾标记：

[ ] 🔳 Arrays & Hashing

[ ] 🔳 Two Pointers

[ ] 🔳 Sliding Window

[ ] 🔳 Stack

[ ] 🔳 Binary Search

[ ] 🔳 Linked List

[ ] 🔳 Trees

[ ] 🔳 Heap / Priority Queue

[ ] 🔳 Backtracking

[ ] 🔳 Tries

[ ] 🔳 Graphs

[ ] 🔳 Advanced Graphs

[ ] 🔳 1-D Dynamic Programming

[ ] 🔳 2-D Dynamic Programming

[ ] 🔳 Greedy

[ ] 🔳 Bit Manipulation

自律即自由，2027春招，顶峰相见！