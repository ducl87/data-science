# DataScience Note| 数据科学学习笔记

记录自己数据科学的学习过程，主要分为数据获取、数据处理、可视化、练手项目等。博客链接：[https://enpeizhao.github.io/tags/#data-science](https://enpeizhao.github.io/tags/#data-science)

因为在工作中经常与数据打交道，同时也对火热的机器学习、大数据等新技术感兴趣，但摸索了很久，一直没什么进步。一直处于兴头来了学一点，遇到不会的就Google，遇到较难的就退缩的状态。

后来看到一句话“**老老实实把基础打牢，否则你有解不完的问题**”，深以为然。我决心系统性地梳理一下，东西比较散乱，也是自己摸索的过程，分享出来希望能逼着自己不断去整理知识体系。

[toc]

### 目录

* 一、数据获取
  * 1.1 开放数据 
  * 1.2 爬虫相关知识
* 二、数据分析
  * 2.1 数学基础
  * 2.2 scikit-learn学习笔记
* 三、练手小项目

## 一、数据获取

### 1.1 开放数据 



### 1.2 爬虫相关知识

| 分类       | 内容                                 | 链接                                                         | 状态                                                         | 更新时间   |
| ---------- | ------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- |
| 基本知识   | HTTP                                 | [HTTP简介](https://enpeizhao.github.io/2021/07/01/http%E7%AE%80%E4%BB%8B/) | ![](https://img.shields.io/badge/%E6%96%87%E7%A8%BF-%E5%B7%B2%E5%AE%8C%E6%88%90-success) | 2021-07-01 |
|            |                                      | [Http headers简介](https://enpeizhao.github.io/2021/07/07/http-headers%E7%AE%80%E4%BB%8B/) | ![](https://img.shields.io/badge/%E6%96%87%E7%A8%BF-%E5%B7%B2%E5%AE%8C%E6%88%90-success) | 2021-07-07 |
|            |                                      | http 重定向Redirections简介                                  |                                                              |            |
|            | HTML                                 | [HTML简介](https://enpeizhao.github.io/2021/07/02/html%E7%AE%80%E4%BB%8B/) | ![](https://img.shields.io/badge/%E6%96%87%E7%A8%BF-%E5%B7%B2%E5%AE%8C%E6%88%90-success) | 2021-07-02 |
|            |                                      | CSS选择器                                                    |                                                              |            |
|            |                                      | xpath选择器                                                  |                                                              |            |
|            |                                      | [一文了解Beautiful Soup基本和高级用法](https://enpeizhao.github.io/2021/07/26/%E4%B8%80%E6%96%87%E4%BA%86%E8%A7%A3beautiful-soup%E5%9F%BA%E6%9C%AC%E5%92%8C%E9%AB%98%E7%BA%A7%E7%94%A8%E6%B3%95/) |                                                              |            |
|            | 正则表达式                           |                                                              |                                                              |            |
| 服务端渲染 | urllib3、pycurl、requests、hyper等： | [urllib3简介](https://enpeizhao.github.io/2021/07/02/urllib3%E7%AE%80%E4%BB%8B/) | ![](https://img.shields.io/badge/%E6%96%87%E7%A8%BF-%E5%B7%B2%E5%AE%8C%E6%88%90-success) ![](https://img.shields.io/badge/%E4%BB%A3%E7%A0%81-%E5%B7%B2%E9%AA%8C%E8%AF%81-success) | 2021-07-02 |
|            |                                      | [PycURL简介](https://enpeizhao.github.io/2021/07/04/pycurl%E7%AE%80%E4%BB%8B/) | ![](https://img.shields.io/badge/%E6%96%87%E7%A8%BF-%E5%B7%B2%E5%AE%8C%E6%88%90-success)![](https://img.shields.io/badge/%E4%BB%A3%E7%A0%81-%E5%B7%B2%E9%AA%8C%E8%AF%81-success) | 2021-07-04 |
|            |                                      | [一文了解requests基本和高级用法](https://enpeizhao.github.io/2021/07/05/%E4%B8%80%E6%96%87%E4%BA%86%E8%A7%A3requests%E5%9F%BA%E6%9C%AC%E5%92%8C%E9%AB%98%E7%BA%A7%E7%94%A8%E6%B3%95/) | ![](https://img.shields.io/badge/%E6%96%87%E7%A8%BF-%E5%B7%B2%E5%AE%8C%E6%88%90-success)![](https://img.shields.io/badge/%E4%BB%A3%E7%A0%81-%E5%B7%B2%E9%AA%8C%E8%AF%81-success) | 2021-07-06 |
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

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210714155611.png?x-oss-process=style/wp)

| 分类     | 内容                                                         | 状态                                                         | 更新时间 |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------- |
| 统计学   |                                                              |                                                              |          |
| 线性代数 | [机器学习相关线性代数简介](https://enpeizhao.github.io/2021/07/12/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E7%9B%B8%E5%85%B3%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0%E7%AE%80%E4%BB%8B/) | ![](https://img.shields.io/badge/%E6%96%87%E7%A8%BF-%E8%BF%9B%E8%A1%8C%E4%B8%AD-orange) |          |
| 概率论   |                                                              |                                                              |          |
| 其他     | 数学公式及符号等                                             | ![](https://img.shields.io/badge/%E6%96%87%E7%A8%BF-%E8%BF%9B%E8%A1%8C%E4%B8%AD-orange) |          |



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
| 分类 \| 奇异值检测 | [除了今日头条，还有哪些APP会被通报整改？](https://enpeizhao.github.io/2021/07/01/%E9%99%A4%E4%BA%86%E4%BB%8A%E6%97%A5%E5%A4%B4%E6%9D%A1-%E8%BF%98%E6%9C%89%E5%93%AA%E4%BA%9Bapp%E4%BC%9A%E8%A2%AB%E9%80%9A%E6%8A%A5%E6%95%B4%E6%94%B9/) | ✅    | ✅    | [YouTube](https://www.youtube.com/watch?v=lqpObIe-sM8&t=9s) \| [B站](https://www.bilibili.com/video/BV1Wq4y1s7XU) |

