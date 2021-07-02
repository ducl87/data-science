# HTML简介

> 编辑时间：2021-07-02



* 引言
* HTML到底是什么？
* HTML文档基本结构
* HTML 元素
  * HTML元素的组成
    * 一般规则
    * 特例
  * HTML元素的嵌套
  * HTML元素的属性
  * 常见的HTML元素

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

#### 一般规则

* **开始标签**：如`<p>This is a paragrah. </p>`中的`<p>`，括号中的`p`是标签名称
* **内容**：如`<p>This is a paragrah. </p>`中的`This is a paragraph.`，标签中的内容会显示在浏览器中；
* **结束标签**：如`<p>This is a paragrah. </p>`中的`</p>`，结束标签比开始标签`<p>`多了一个`/`。

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210702115148.png?x-oss-process=style/wp)



#### 特例

也有很多标签没有结束标签，如`<img>, <input> <br> <hr>`等，这些标签通过标签的属性显示相关内容。

```html
<!--显示图片-->
<img src='https://img1.doubanio.com/img/files/file-1624939019.jpg'>
<!--输入框-->
<input type="text" placeholder="书籍、电影、音乐、小组、小站、成员" >
```



### HTML元素的嵌套

HTML的一个元素可以嵌套在另一个元素内，如下图中，`<h4>,<ul>`标签嵌套在`<div>`中，而`<li>`又嵌套在`<ul>`中。

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210702142038.png?x-oss-process=style/wp)



在真实网页中，嵌套关系可能非常复杂，网页的设计者需要提前规划好网页布局。我们在浏览器源码中可以点击展开箭头查看嵌套的子元素。

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210702142441.png?x-oss-process=style/wp)



### HTML元素的属性

```html
<input type="text" placeholder="书籍、电影、音乐、小组、小站、成员" >
```

HTML元素也有自己的属性，如`<input>`标签的`type`属性是`text`，属性一般以`属性名 = 属性值`插入开始标签内。

一个元素可以插入多个属性，比如上面的代码中`<input>`的另一个`placeholder`属性。



### 常见的HTML元素

HTML总共约有[100多种元素](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)，但常用的一般只有约20个，分为以下5类：

* 区域布局类

```html
 <div>, <span>, <header>, <footer>, <nav>, <main>, <section> 
```

* 文本类

```html
  <h1> to <h6>, <p>, <div>, <span>, <ul>, <ol>, <li>
```

* 表单类

```html
  <form>, <input>, <button>, <label>, <textarea>
```

* 图片和超链接

```html
  <img>, <a>
```

* 其他

```html
  <br>, <hr>
```



------

参考信息

* [HTML | Basics](https://www.geeksforgeeks.org/html-basics/)
* [Learn HTML Basics for Beginners in Just 15 Minutes](https://www.freecodecamp.org/news/html-basics-for-beginners/)







