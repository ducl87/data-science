# 每天都用的HTTP到底是什么？



[toc]

### 目录：

* 概览
* [HTTP系统的组成部分](#http系统的组成部分)
* 

## 概览

简单来说，HTTP（HyperText Transfer Protocol，超文本传输协议）是一种网络传输协议，它可以用来传输各种网络资源，常见的HTML文档、图片、视频、文件等都可以用HTTP传输。



如下图，我们访问一个网站时大致的流程如下：

* 在浏览器（web browser）中输入一个网址URL，浏览器请求（request）服务器获取HTML文档；
* 服务器响应（response）请求，并返回对应HTML文档；
* 浏览器根据HTML渲染页面，页面中有图片，视频，样式CSS，广告等资源，这些资源可能分布在不同的服务器上；
* 浏览器会分别根据资源的URL请求对应服务器，获取对应资源加载显示。





![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210701115008.png?x-oss-process=style/wp)





## [HTTP系统的组成部分]()

HTTP是一种“客户端-服务器”协议：一次完整的请求（**request**）由客户端（**user-agent**）向服务器（**server**）发出，服务器再返回响应信息（**response**）。

大多数时候，user-agent都是web浏览器，但理论上它没有限制，比如我们要开发的网络爬虫（robot spider）就可以是一个user-agent，他也可以向服务器发出请求，这个也是爬虫工作的基础。

在真实情况下，客户端和服务器还有很多服务或组件，统称代理（**proxies**），一般用作缓存、过滤、负载均衡等。

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210701144551.png?x-oss-process=style/wp)



我们往更底层看，在你电脑浏览器访问一个网站，向服务器发起HTTP请求时，其实数据要经过一堆路由器、交换机等设备，但好在http是构架传输层协议TCP之上的应用层协议，我们可以“无视”这些传输设备、传输层协议，更加聚焦HTTP业务本身。

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210701142231.png?x-oss-process=style/wp)



### 客户端 Client: the user-agent

**user-agent** 理论上可以使任何代表用户（user）的工具或服务，浏览器、网络开发工具、爬虫是常见的user-agent



### 网络服务器 web server

用于响应客户端请求的服务器，它是一个泛称，现如今，为了返回一次请求，可能要查询很多台机器（缓存、数据库、队列等）。



### 代理 proxies







## 错误码

[原文链接](https://docs.python.org/3/howto/urllib2.html#error-codes)

```python
# Table mapping response codes to messages; entries have the
# form {code: (shortmessage, longmessage)}.
responses = {
    100: ('Continue', 'Request received, please continue'),
    101: ('Switching Protocols',
          'Switching to new protocol; obey Upgrade header'),

    200: ('OK', 'Request fulfilled, document follows'),
    201: ('Created', 'Document created, URL follows'),
    202: ('Accepted',
          'Request accepted, processing continues off-line'),
    203: ('Non-Authoritative Information', 'Request fulfilled from cache'),
    204: ('No Content', 'Request fulfilled, nothing follows'),
    205: ('Reset Content', 'Clear input form for further input.'),
    206: ('Partial Content', 'Partial content follows.'),

    300: ('Multiple Choices',
          'Object has several resources -- see URI list'),
    301: ('Moved Permanently', 'Object moved permanently -- see URI list'),
    302: ('Found', 'Object moved temporarily -- see URI list'),
    303: ('See Other', 'Object moved -- see Method and URL list'),
    304: ('Not Modified',
          'Document has not changed since given time'),
    305: ('Use Proxy',
          'You must use proxy specified in Location to access this '
          'resource.'),
    307: ('Temporary Redirect',
          'Object moved temporarily -- see URI list'),

    400: ('Bad Request',
          'Bad request syntax or unsupported method'),
    401: ('Unauthorized',
          'No permission -- see authorization schemes'),
    402: ('Payment Required',
          'No payment -- see charging schemes'),
    403: ('Forbidden',
          'Request forbidden -- authorization will not help'),
    404: ('Not Found', 'Nothing matches the given URI'),
    405: ('Method Not Allowed',
          'Specified method is invalid for this server.'),
    406: ('Not Acceptable', 'URI not available in preferred format.'),
    407: ('Proxy Authentication Required', 'You must authenticate with '
          'this proxy before proceeding.'),
    408: ('Request Timeout', 'Request timed out; try again later.'),
    409: ('Conflict', 'Request conflict.'),
    410: ('Gone',
          'URI no longer exists and has been permanently removed.'),
    411: ('Length Required', 'Client must specify Content-Length.'),
    412: ('Precondition Failed', 'Precondition in headers is false.'),
    413: ('Request Entity Too Large', 'Entity is too large.'),
    414: ('Request-URI Too Long', 'URI is too long.'),
    415: ('Unsupported Media Type', 'Entity body in unsupported format.'),
    416: ('Requested Range Not Satisfiable',
          'Cannot satisfy request range.'),
    417: ('Expectation Failed',
          'Expect condition could not be satisfied.'),

    500: ('Internal Server Error', 'Server got itself in trouble'),
    501: ('Not Implemented',
          'Server does not support this operation'),
    502: ('Bad Gateway', 'Invalid responses from another server/proxy.'),
    503: ('Service Unavailable',
          'The server cannot process the request due to a high load'),
    504: ('Gateway Timeout',
          'The gateway server did not receive a timely response'),
    505: ('HTTP Version Not Supported', 'Cannot fulfill request.'),
    }
```





参考信息：

[1]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview	"An overview of HTTP"

