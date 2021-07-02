# data-science | 数据科学

记录自己数据科学的学习过程，主要分为数据获取、数据处理、可视化等模块

持续整理中。。。

**目录**

- [ ] 数据获取
  - [ ] 爬虫相关知识
  - [ ] 开源数据集
- [ ] 数据分析
  - [ ] 基本工具：pandas等
  - [ ] 了解基本机器学习模型：sklearn整理好
  - [ ] 感受前沿：kaggle案例准备各种类型准备3篇
- [ ] 真实案例
- [ ] 可视化

------



## 爬虫相关知识

* 基本知识：
  * HTTP：
    * [HTTP简介](./contents/0.basic/HTTP简介.md)
    * 在Chrome分析HTTP
  * HTML
    * HTML简介

- 分析页面渲染方式

- - 服务端渲染：结果都在HTML中

  - - urllib、urllib3、pycurl、hyper、requests、grab等：

  - 客户端渲染：JS渲染，也可能AJAX获取

  - - 寻找ajax接口

    - - chrome开发者工具
      - Fiddler/Charles 设置代理抓包

    - 模拟浏览器执行

    - - selenium
      - splinter
      - spynner / Ghost.py
      - pyppeteer
      - PhantomJS
      - Splash
      - requests-html

    - 直接提取JavaScript

    - - 正则表达式

    - 模拟执行JavaScript

    - - selenium：使用execute_script方法执行，return可获取执行结果
      - PyExecJS
      - js2py
      - PyV8

- * 爬虫框架：
    * scrapy

- 爬取APP

- - 普通接口（接口无加密）：

  - - Charles / fiddler / mitmproxy 直接代理抓HTTP/ HTTPS包

  - 加密参数接口：

  - - Fiddler：对接C#实时处理脚本处理
    - mitmdump：对接Python脚本实时处理
    - Xposed：使用hook来直接获取结果
    - 直接破解：直接破解加密参数构造规则

  - 加密内容接口：

  - - Appium：类似selenium，可见即可爬
    - Xposed：使用hook来直接获取结果
    - 反编译：找出加密算法，然后直接模拟
    - 改写手机底层：直接修改操作系统源码

  - 非常规协议：

  - - wireshark：抓取所有协议的包
    - TCPdump：抓取TCP数据包

- 防反爬

- - 手机站点或APP站点：反爬较弱
  - 免费代理：爬取免费代理使用，可用率极低
  - 付费代理：可用率高，推荐：讯代理、阿布云代理、多贝云代理、芝麻代理
  - 维护代理池：使用免费或付费代理自己维护代理池
  - ADSL代理：使用ADSL拨号主机搭建代理池，推荐：云立方
  - Tor代理：暗网代理，速度慢
  - Socks代理：速度较快





### 练手小项目：

| 类别               | 名称                                                         | 数据 | 源码 | 视频地址                                                     |
| ------------------ | ------------------------------------------------------------ | ---- | ---- | ------------------------------------------------------------ |
| 分类 \| 奇异值检测 | [除了今日头条，还有哪些APP会被通报整改？](./projects/android_malware_analysis) | ✅    | ✅    | [YouTube](https://www.youtube.com/watch?v=lqpObIe-sM8&t=9s) \| [B站](https://www.bilibili.com/video/BV1Wq4y1s7XU) |

