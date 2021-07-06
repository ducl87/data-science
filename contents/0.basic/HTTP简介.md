# HTTP简介

> 更新时间：2021-07-01
>

### 目录

* [概览](#概览)
* [HTTP系统的组成部分](#http系统的组成部分)
  * [客户端 Client: the user-agent](#客户端-client-the-user-agent)
  * [网络服务器 web server](#网络服务器-web-server)
  * [代理 proxies](#代理-proxies)
* [HTTP工作流](#http工作流)
* [HTTP消息（Messages）](#http消息messages)

------



## 概览

简单来说，HTTP（HyperText Transfer Protocol，超文本传输协议）是一种网络传输协议，它可以用来传输各种网络资源，常见的HTML文档、图片、视频、文件等都可以用HTTP传输。



如下图，我们访问一个网站时大致的流程如下：

* 在浏览器（web browser）中输入一个网址URL，浏览器请求（request）服务器获取HTML文档；
* 服务器响应（response）请求，并返回对应HTML文档；
* 浏览器根据HTML渲染页面，页面中有图片，视频，样式CSS，广告等资源，这些资源可能分布在不同的服务器上；
* 浏览器会分别根据资源的URL请求对应服务器，获取对应资源加载显示。





![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210701115008.png?x-oss-process=style/wp)





## HTTP系统的组成部分

HTTP是一种“客户端-服务器”协议：一次完整的请求（**request**）由客户端（**user-agent**）向服务器（**server**）发出，服务器再返回响应信息（**response**）。

大多数时候，user-agent都是web浏览器，但理论上它没有限制，比如我们要开发的网络爬虫（robot spider）就可以是一个user-agent，他也可以向服务器发出请求，这个也是爬虫工作的基础。

在真实情况下，客户端和服务器还有很多服务或组件，统称代理（**proxies**），一般用作缓存、过滤、负载均衡等。

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210701144551.png?x-oss-process=style/wp)



我们往更底层看，在你电脑浏览器访问一个网站，向服务器发起HTTP请求时，其实数据要经过一堆路由器、交换机等设备，但好在http是传输层协议TCP之上的应用层协议，我们可以“无视”这些传输设备、传输层协议，更加聚焦HTTP业务本身。

<img src="https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210701142231.png?x-oss-process=style/wp" style="zoom: 33%;" />



### 客户端 Client: the user-agent

**user-agent** 理论上可以使任何代表用户（user）的工具或服务，浏览器、网络开发工具、爬虫是常见的user-agent



### 网络服务器 web server

用于响应客户端请求的服务器，它是一个泛称，现如今，为了返回一次请求，可能要查询很多台机器（缓存、数据库、队列等）。



### 代理 proxies

在浏览器和服务器间，有大量电脑、机器等设备辅助传递HTTP消息，其中大部分都在传输层、网络层、物理层，HTTP协议运行其上，这些服务或组件统称为**代理（proxies）**。

**代理的分类：**

* 透明，仅传递HTTP信息，不更改其信息；
* 不透明，在消息传递给服务器或客户端前修改HTTP信息。

作用：

* 缓存 caching （如浏览器缓存）；
* 过滤 filtering （如反病毒扫描服务和青少年权限管理）；
* 负载均衡 load balancing （将并发的请求分解到不同服务器上应答）；
* 认证 authentication （控制访问不同资源的权限）；
* 日志记录 logging （记录历史信息）。



## HTTP工作流

客户端向服务器发起HTTP请求具体流程如下：

1. **建立TCP连接**： TCP连接用于发送请求、接收响应消息。客户端可以随时建立新的TCP连接，复用已经存在的连接，或者建立多个连接；
2. **发送HTTP消息：** HTTP/2 版本之前的HTTP消息是明码直接可读的（如下图），从HTTP/2 开始，HTTP消息被组装进二进制框架（Binary framing)，以提高传输效率、安全性、压缩率等。

<img src="https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210701174852.png?x-oss-process=style/wp" style="zoom:50%;" />

<img src="https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210701174353.png?x-oss-process=style/wp" style="zoom:67%;" />



但基本原理都是一样的，比如：

```
GET / HTTP/1.1
Host: developer.mozilla.org
Accept-Language: fr
```

3. **读取服务器返回的消息**，比如：

```
HTTP/1.1 200 OK
Date: Sat, 09 Oct 2010 14:28:02 GMT
Server: Apache
Last-Modified: Tue, 01 Dec 2009 20:18:22 GMT
ETag: "51142bc1-7449-479b075b2891b"
Accept-Ranges: bytes
Content-Length: 29769
Content-Type: text/html

<!DOCTYPE html... (here comes the 29769 bytes of the requested web page)
```

4. 关闭连接，或者复用该连接给新的HTTP请求。



## HTTP消息（Messages）

### 请求（requests）消息

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210701175454.png?x-oss-process=style/wp)



请求消息包含以下元素：

* **HTTP请求方法（method）**：请求方法表示客户端对服务器上的资源希望执行的动作，常见方法有：GET、POST、PUT、DELETE等
* **请求地址（URL）**：一般指我们常说的网址，根据HTTP规定，它可以包含以下元素：协议名（http/https）、域名获取IP、端口、路径、参数、锚点

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210701180337.png?x-oss-process=style/wp)

* **HTTP协议的版本**
* **头信息 headers**：提供给服务器的额外信息，如User-Agent（告诉自己浏览器版本、型设备型号等）、Accept-Language（语言要求）、Accept-Encoding（编码要求）等；
* **表单信息等数据**：如使用POST请求时，需要将表单数据、待上传的文件等资源一同发送

### 响应（responses）消息

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210701181313.png?x-oss-process=style/wp)

响应消息包含以下元素：

* **HTTP版本**
* **状态码**：显示请求的状态，如成功、失败、未找到地址等，一般有如下几类
  * 信息类（100 - 199）
  * 成功类（200 - 299）
  * 重定向 （300 - 399）
  * 客户端错误（400 - 499）
  * 服务器错误（500 - 599）

* **头信息 headers**：类似请求的头信息
* **消息体 body**：包含返回资源



------

参考信息：

* [An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview )
* [TCP/IP、HTTP协议的区别](TCP/IP、HTTP协议的区别)
* [HTTP/1.x vs. HTTP/2 – The Difference Between the Two Protocols Explained](https://cheapsslsecurity.com/p/http2-vs-http1/)

* [What is a URL?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL)

