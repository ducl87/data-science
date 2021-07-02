# HTML简介

[toc]



## 引言

在浏览器打开一个网站（如 https://www.douban.com/），查看源码，我们一般会看到一堆英文和中文搭配的代码，这些代码就是HTML代码（可能也有部分CSS、JS代码等）。

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210702110526.png?x-oss-process=style/wp)



可以看到，HTML代码中的文字信息和网页显示一一对应，爬虫抓取网页信息时，就是提取HTML代码中对应的信息。

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210702112140.png?x-oss-process=style/wp)





## HTML到底是什么？

HTML（Hypertext Markup Language），全称超文本**标记**语言，这是一种很简单、容错性很高的语言，浏览器就是根据HTML代码渲染对应网页信息的。

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210702113407.png?x-oss-process=style/wp)



## HTML文档基本结构



```html
<!DOCTYPE html>
<html>
<head>
    <!-- Information about the page -->
    <!--This is the comment tag-->
    <title>这个是标题</title>
</head>
<body>
    <!--Contents of the webpage-->
</body>
</html>
```

如上面HTML代码片段：

* 每个HTML文档都是以一个 `<html>`标签开始，一般也会在前面加上`<!DOCTYPE html>`；
* **`<html>`**： 每个完整的HTML代码都是包含在 html 标签之间，以`<html>`开始，并以`</html>`结尾；
* **`<head>`：** head标签中一般包含 HTML页面的基本信息，如标题、样式、描述等，这些信息不会显示在浏览器窗口中；
* **`<body>`：**body标签中的内容会显示浏览器中，如文本、图片、视频等。



## HTML 元素

### HTML元素的组成

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210702115148.png?x-oss-process=style/wp)



### HTML元素的嵌套组合

### HTML元素的属性

### 常见的HTML元素











------

参考信息

* [HTML | Basics](https://www.geeksforgeeks.org/html-basics/)
* [Learn HTML Basics for Beginners in Just 15 Minutes](https://www.freecodecamp.org/news/html-basics-for-beginners/)







