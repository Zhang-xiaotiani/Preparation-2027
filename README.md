# 🚗 Didi-Preparation-2027

> **目标：** 2027年3月后跳槽回归互联网，斩获 **滴滴-网约车核心业务部-测试开发工程师** Offer。
> **策略：** 滚雪球式复习，硬核技术输出，定向场景爆破。

---

## 📅 备战时间线与工作目录指南

| 备战阶段 | 核心时间 | 重点工作目录 | 阶段阶段性目标 |
| :--- | :--- | :--- | :--- |
| **第一阶段：底层筑基** | 2026.06 - 2026.07 | `01_Algorithms/`<br>`02_Python_Advanced/` | 攻克 LeetCode 基础题；吃透 Python 协程/高级特性与 Pytest 框架源码。 |
| **第二阶段：工程效能** | 2026.08 - 2026.10 | `01_Algorithms/`<br>`03_Engineering_Efficiency/` | 搞定 Locust 压测与 FastAPI Mock 开发；掌握 Redis 分布式锁与 MQ 测试要点。 |
| **第三阶段：场景爆破** | 2026.11 - 2027.01 | `01_Algorithms/`<br>`04_Business_Scenarios/` | 深入网约车核心订单状态机、LBS 场景；对齐滴滴历年测开面经查漏补缺。 |
| **第四阶段：实战冲刺** | 2027.02 - 2027.03+ | `04_Business_Scenarios/`<br>`05_Daily_Review/` | 精修 STAR 法则简历；全开内推渠道，迎战面试。 |

---

## 📂 目录职责与规范说明

### 📁 01_Algorithms (算法刷题归档)
* **活跃周期：** 2026.06 - 2027.03 (贯穿全程，每天打卡)
* **子目录说明：**
    * `LeetCode/`：存放每日一题、分类专项（链表、二叉树、滑动窗口等）的 Python 解题代码。
    * `Interview_Top100/`：临考前 1-2 个月，重点攻克大厂高频手撕真题。
* **规范：** 每个代码文件建议以题号命名（如 `lc_0001_two_sum.py`），并在文件头部以注释形式记录思路和时空复杂度。

### 📁 02_Python_Advanced (Python 进阶与自动化)
* **活跃周期：** 2026.06 - 2026.07 (第 1-2 个月)
* **子目录说明：**
    * `basic_features/`：深入理解 GIL 锁、装饰器、多进程、`asyncio` 异步编程的实验与测试代码。
    * `pytest_framework/`：Pytest 自定义插件编写、Fixture 核心机制研究及自动化脚手架封装。

### 📁 03_Engineering_Efficiency (工程效能与中间件)
* **活跃周期：** 2026.08 - 2026.10 (第 3-5 个月)
* **子目录说明：**
    * `mock_services/`：利用 FastAPI/Flask 编写的高性能 Mock 服务，模拟网约车下游依赖。
    * `load_testing/`：Locust 压测脚本、分布式施压配置及性能测试报告。
    * `middleware_practice/`：Redis 分布式锁模拟（防重复下单/抢单场景）、Kafka/RabbitMQ 消息积压与死信队列测试 Demo。

### 📁 04_Business_Scenarios (滴滴网约车场景与面经)
* **活跃周期：** 2026.11 - 2027.01 (第 6-8 个月)
* **子目录说明：**
    * `order_statemachine/`：梳理网约车下单-派单-接单全链路状态机，记录并发冲突与异常流测试方案。
    * `lbs_testing/`：GPS 漂移、电子围栏边界、ETA 算法测试设计文档与 Mock 方案。
    * `didi_面经/`：归纳总结滴滴近两年的测开面经，逐条进行对线通关。

### 📁 05_Daily_Review (复盘与简历准备)
* **活跃周期：** 2026.06 - 2027.03 (全程周复盘 + 冲刺期核心)
* **子目录说明：**
    * `weekly_kpt/`：每周日进行 KPT（Keep, Problem, Try）复盘文档。
    * `resume_materials/`：存放简历的迭代版本，以及用 STAR 法则沉淀的项目亮点素材库。

---

## ⏱️ 今日看板 (Today's To-Do)
- [ ] 确认本地 Python 环境及常用的 Lint 工具（如 flake8 / black）配置完毕。
- [ ] 在 `01_Algorithms/LeetCode/` 下提交第一道算法题，点亮 GitHub/Gitee 绿墙！

---
*自律即自由，2027春招，顶峰相见！*
