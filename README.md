# DataScience Note| 数据科学学习笔记

记录自己数据科学的学习过程，主要分为数据获取、数据处理、可视化、练手项目等。

因为在工作中经常与数据打交道，同时也对火热的机器学习、大数据等新技术感兴趣，但摸索了很久，一直没什么进步。一直处于兴头来了学一点，遇到不会的就Google，遇到较难的就退缩的状态。

后来看到一句话“**老老实实把基础打牢，否则你有解不完的问题**”，深以为然。我决心系统性地梳理一下，东西比较散乱，也是自己摸索的过程，分享出来希望能逼着自己不断去整理知识体系。

[toc]

### 目录

* 一、数据获取
  * 1.1 开放数据 
  * 1.2 爬虫相关知识
* 二、数据分析
  * 2.1 scikit-learn学习笔记
* 三、练手小项目

## 一、数据获取

### 1.1 开放数据 



### 1.2 爬虫相关知识

| 分类       | 内容                                 | 链接                                                         | 状态                                                         | 更新时间   |
| ---------- | ------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- |
| 基本知识   | HTTP                                 | [HTTP简介](./contents/0.basic/HTTP简介.md)                   | ![](https://img.shields.io/badge/%E6%96%87%E7%A8%BF-%E5%B7%B2%E5%AE%8C%E6%88%90-success) | 2021-07-01 |
|            |                                      | [Http headers简介](./contents/0.basic/http_headers简介.md)   | ![](https://img.shields.io/badge/%E6%96%87%E7%A8%BF-%E5%B7%B2%E5%AE%8C%E6%88%90-success) | 2021-07-07 |
|            |                                      | http 重定向Redirections简介                                  |                                                              |            |
|            | HTML                                 | [HTML简介](./contents/0.basic/HTML简介.md)                   | ![](https://img.shields.io/badge/%E6%96%87%E7%A8%BF-%E5%B7%B2%E5%AE%8C%E6%88%90-success) | 2021-07-02 |
|            |                                      | CSS选择器                                                    |                                                              |            |
|            |                                      | xpath选择器                                                  |                                                              |            |
|            |                                      | Beautiful Soup 解析HTML                                      |                                                              |            |
|            | 正则表达式                           |                                                              |                                                              |            |
| 服务端渲染 | urllib3、pycurl、requests、hyper等： | [urllib3简介](./contents/1.server_rendered/0.urllib3简介.md) | ![](https://img.shields.io/badge/%E6%96%87%E7%A8%BF-%E5%B7%B2%E5%AE%8C%E6%88%90-success) ![](https://img.shields.io/badge/%E4%BB%A3%E7%A0%81-%E5%B7%B2%E9%AA%8C%E8%AF%81-success) | 2021-07-02 |
|            |                                      | [PycURL简介](./contents/1.server_rendered/1.PycURL简介.md)   | ![](https://img.shields.io/badge/%E6%96%87%E7%A8%BF-%E5%B7%B2%E5%AE%8C%E6%88%90-success)![](https://img.shields.io/badge/%E4%BB%A3%E7%A0%81-%E5%B7%B2%E9%AA%8C%E8%AF%81-success) | 2021-07-04 |
|            |                                      | [一文了解requests基本和高级用法](./contents/1.server_rendered/2.一文了解requests基本和高级用法.md) | ![](https://img.shields.io/badge/%E6%96%87%E7%A8%BF-%E5%B7%B2%E5%AE%8C%E6%88%90-success)![](https://img.shields.io/badge/%E4%BB%A3%E7%A0%81-%E5%B7%B2%E9%AA%8C%E8%AF%81-success) | 2021-07-06 |
| 客户端渲染 | 寻找ajax接口                         | chrome开发者工具                                             |                                                              |            |
|            |                                      | Fiddler/Charles 设置代理抓包                                 |                                                              |            |
|            | 模拟浏览器执行                       | - selenium<br/>- splinter<br/>- spynner / Ghost.py<br/>- pyppeteer<br/>- PhantomJS<br/>- Splash<br/>- requests-html |                                                              |            |
|            | 直接提取JavaScript                   | 正则表达式                                                   |                                                              |            |
|            | 模拟执行JavaScript                   | - selenium：使用execute_script方法执行，return可获取执行结果<br/>- PyExecJS<br/>- js2py<br/>- PyV8 |                                                              |            |
| 爬虫框架   | scrapy                               | scrapy                                                       |                                                              |            |
| 爬取APP    | 普通接口（接口无加密）：             | Charles / fiddler / mitmproxy 直接代理抓HTTP/ HTTPS包        |                                                              |            |
|            | 加密参数接口                         | Fiddler：对接C#实时处理脚本处理                              |                                                              |            |
|            |                                      | mitmdump：对接Python脚本实时处理                             |                                                              |            |
|            |                                      | Xposed：使用hook来直接获取结果                               |                                                              |            |
|            |                                      | 直接破解：直接破解加密参数构造规则                           |                                                              |            |
|            | 加密内容接口                         | Appium：类似selenium，可见即可爬                             |                                                              |            |
|            |                                      | Xposed：使用hook来直接获取结果                               |                                                              |            |
|            |                                      | 反编译：找出加密算法，然后直接模拟                           |                                                              |            |
|            |                                      | 改写手机底层：直接修改操作系统源码                           |                                                              |            |
| 非常规协议 | wireshark：抓取所有协议的包          |                                                              |                                                              |            |
|            | TCPdump：抓取TCP数据包               |                                                              |                                                              |            |
| 防反爬     |                                      | - 手机站点或APP站点：反爬较弱<br/>  - 免费代理：爬取免费代理使用，可用率极低<br/>  - 付费代理：可用率高，推荐：讯代理、阿布云代理、多贝云代理、芝麻代理<br/>  - 维护代理池：使用免费或付费代理自己维护代理池<br/>  - ADSL代理：使用ADSL拨号主机搭建代理池，推荐：云立方<br/>  - Tor代理：暗网代理，速度慢<br/>  - Socks代理：速度较快 |                                                              |            |



## 二、数据分析

### 2.1 数学基础

| 分类     | 内容                                                         | 状态                                                         | 更新时间 |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------- |
| 统计学   |                                                              |                                                              |          |
| 线性代数 | [机器学习相关线性代数简介](./contents/2.1.math/机器学习相关线性代数简介.html) | ![](https://img.shields.io/badge/%E6%96%87%E7%A8%BF-%E8%BF%9B%E8%A1%8C%E4%B8%AD-orange) |          |
| 概率论   |                                                              |                                                              |          |
|          |                                                              |                                                              |          |

### 2.2 scikit-learn学习笔记

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210707164807.png?x-oss-process=style/wp)

| 分类                             | 内容                                                         | 状态                                                         | 更新时间   |
| -------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- |
| 基本知识                         | [Scikit-Learn简介](./contents/2.2.scikit-learn/Scikit-Learn简介.md) | ![](https://img.shields.io/badge/%E6%96%87%E7%A8%BF-%E5%B7%B2%E5%AE%8C%E6%88%90-success) ![](https://img.shields.io/badge/%E4%BB%A3%E7%A0%81-%E5%B7%B2%E9%AA%8C%E8%AF%81-success) | 2021-07-08 |
| 分类（classification）           | Logistic Regression                                          |                                                              |            |
|                                  | Support Vector Machine                                       |                                                              |            |
|                                  | Naive Bayes (Gaussian, Multinomial)                          |                                                              |            |
|                                  | Stochastic Gradient Descent Classifier                       |                                                              |            |
|                                  | KNN (k-nearest neighbor)                                     |                                                              |            |
|                                  | Decision Tree                                                |                                                              |            |
|                                  | Random Forest                                                |                                                              |            |
|                                  | Gradient Boosting Classifier                                 |                                                              |            |
|                                  | LGBM Classifier                                              |                                                              |            |
|                                  | XGBoost Classifier                                           |                                                              |            |
| 回归（regression）               | Linear Regression                                            |                                                              |            |
|                                  | LGBM Regressor                                               |                                                              |            |
|                                  | XGBoost Regressor                                            |                                                              |            |
|                                  | CatBoost Regressor                                           |                                                              |            |
|                                  | Stochastic Gradient Descent Regression                       |                                                              |            |
|                                  | Kernel Ridge Regression                                      |                                                              |            |
|                                  | Elastic Net Regression                                       |                                                              |            |
|                                  | Bayesian Ridge Regression                                    |                                                              |            |
|                                  | Gradient Boosting Regression                                 |                                                              |            |
|                                  | Support Vector Machine                                       |                                                              |            |
|                                  |                                                              |                                                              |            |
| 聚类（clustering）               |                                                              |                                                              |            |
| 降维（dimensionality reduction） |                                                              |                                                              |            |



## 三、练手小项目

| 类别               | 名称                                                         | 数据 | 源码 | 视频地址                                                     |
| ------------------ | ------------------------------------------------------------ | ---- | ---- | ------------------------------------------------------------ |
| 分类 \| 奇异值检测 | [除了今日头条，还有哪些APP会被通报整改？](./projects/android_malware_analysis) | ✅    | ✅    | [YouTube](https://www.youtube.com/watch?v=lqpObIe-sM8&t=9s) \| [B站](https://www.bilibili.com/video/BV1Wq4y1s7XU) |

