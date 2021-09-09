---
layout: post
title: '一文了解Beautiful Soup基本和高级用法'
date: 2021-07-26
tags:
  Beautiful-soup
  html
  Python
  data-science
---



### 目录：

* 一、快速入门Beautiful Soup
* 二、定位目标内容
  * 2.1 向下检索
    * 2.1.1 使用标签名定位
    * 2.1.2 `.contents`和`.children`
    * 2.1.3 `.descendants`
  * 2.2 向上检索
    * 2.2.1 `.parent`
  * 2.3 同级检索
* 三、搜索目标内容
  * 3.1 find_all()
    * 3.1.1 名称（name）
    * 3.1.2 关键字
    * 3.1.3 根据CSS 的类名（class）搜索
    * 3.1.4 字符串（string）
    * 3.1.5 Limit
    * 3.1.6 递归（recursive）
  * 3.2 CSS选择器



## 一、快速入门Beautiful Soup

下面是一段`html`代码：

```html
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were </p>
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
```

安装好`BeautifulSoup`，导入并使用：

```python
# 导入库
from bs4 import BeautifulSoup
# 实例化
soup = BeautifulSoup(html_doc, 'html.parser')

# 获取HTML title
>>> soup.title
<title>The Dormouse's story</title>

# 获取HTML title 内容
>>> soup.title.string
"The Dormouse's story"

# 获取HTML中第一个<p>标签
>>> soup.p
<p class="title"><b>The Dormouse's story</b></p>

# 获取<p>的父标签名称
>>> soup.p.parent.name
'body'

# 获取<p>的class属性
>>> soup.p['class']
['title']

# 获取HTML第一个<a>标签
>>> soup.a
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# 找出HTML所有的<a>标签
>>> soup.find_all('a')
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


# 遍历属性
for link in soup.find_all('a'):
    print(link['href'])
    
http://example.com/elsie
http://example.com/lacie
http://example.com/tillie

  
# 根据属性查找
>>> soup.find(id='link2')
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>


# 获取文本
>>> soup.find_all('p')[1].get_text()
'Once upon a time there were three little sisters; and their names were '

```



## 二、定位目标内容

### 2.1 向下检索

如下图，因为HTML元素具有嵌套结构，可以使用向下搜索的方式快速匹配到目标位置，Beautiful Soup提供了多种方式向下搜搜

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210702142038.png?x-oss-process=style/wp)

继续使用前文HTML代码示例：

```html
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were </p>
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
```



#### 2.1.1 使用标签名定位

```python
# 获取head内的信息
soup.head
# <head><title>The Dormouse's story</title></head>

# 获取title信息
soup.title
# <title>The Dormouse's story</title>

# 可以一直追加
soup.body.b
# <b>The Dormouse's story</b>

# 当有多个重名标签时，会返回第一个
soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

```



#### 2.1.2 `.contents`和`.children`

使用`.contents`会以`list`形式返回标签所有子元素，需要注意`string`文本没有`.contents`，因为文本无法包含子元素

```python
# 获取 head 子元素
soup.head.contents
[<title>The Dormouse's story</title>]

# 挑选出第1个子元素
soup.head.contents[0]
# <title>The Dormouse's story</title>

# 层层递进
soup.head.contents[0].contents[0]
"The Dormouse's story"

# string 没有.contents
soup.head.contents[0].contents[0].contents 

# AttributeError: 'NavigableString' object has no attribute 'contents'
```

也可以使用`.children`遍历子元素：

```python
soup.head.children
# <list_iterator at 0x7ff7e9d3fa50>

for i in soup.head.children:
    print(i)

# <title>The Dormouse's story</title>    
```



#### 2.1.3 `.descendants`

打个比方，`.contents`和`.children`会返回“儿子”元素信息，而`.descendants`会返回所有“子孙”后代信息：

如 `BeautifulSoup` 对象只有1个“儿子”，就是`html`，但他有很多子孙，就是html内部嵌套的元素，用`.descendants`验证：

```python
len(list(soup.children))
# 1
len(list(soup.descendants))
# 28
```

遍历`.descentants`，会得到所有后代信息：

```python
for i in soup.head.descendants:
    print(i)
    
# <title>The Dormouse's story</title>
# The Dormouse's story
```



### 2.2 向上检索

Beautiful Soup也支持从子节点向上检索的方式。

#### 2.2.1 `.parent`

```python
# 获取title
soup.title
# <title>The Dormouse's story</title>

# 获取title父节点
soup.title.parent
# <head><title>The Dormouse's story</title></head>

```

### 2.3 同级检索

假设一段html代码如下：

```python
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c><d>text2</d></b></a>")
print(sibling_soup.prettify())

###
<html>
 <body>
  <a>
   <b>
    text1
   </b>
   <c>
    text2
   </c>
   <d>
    text2
   </d>
  </a>
 </body>
</html>
###
```

使用`.next_sibling`和`.previous_sibling`定位同一级别的元素（兄弟元素）：

```python
# 寻找 b 标签下一级兄弟
sibling_soup.b.next_sibling
# <c>text2</c>

# 寻找 c 标签上一级兄弟
sibling_soup.c.previous_sibling
# <b>text1</b>

```

使用`.next_siblings`和`.previous_siblings`获取多个同级元素：

```python
list(sibling_soup.b.next_siblings)
# [<c>text2</c>, <d>text2</d>]

list(sibling_soup.d.previous_siblings)
# [<c>text2</c>, <b>text1</b>]

```

## 三、搜索目标内容

Beautiful Soup提供了多种方式搜索目标内容，本文主要介绍常用的`find_all()`方法，其他如`find(),find_parents(),find_parent()`等用法与`find_all()`类似。

继续使用前文HTML代码示例：

```html
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were </p>
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
```



### 3.1 find_all()

`find_all(name,attrs,recursive,string,limit,**kwargs)`

`find_all()`会搜索一个节点的所有后代节点，一旦匹配，会返回对应节点：

#### 3.1.1 名称（name）

```python
# 找出所有<a>标签
soup.find_all('a')

[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


# 也支持正则表达式
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
    
# body
# b


# 也支持传入一个list形式的参数：
# 匹配 a,b,title标签
soup.find_all(['a','b','title'])

[<title>The Dormouse's story</title>,
 <b>The Dormouse's story</b>,
 <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


# 函数形式
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

soup.find_all(has_class_but_no_id)
# [<p class="title"><b>The Dormouse's story</b></p>,
#  <p class="story">Once upon a time there were...</p>,
#  <p class="story">...</p>]  
```



#### 3.1.2 关键字

```python
# 关键字=属性
soup.find_all(id='link2')
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]


soup.find_all(href=re.compile("elsie"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]


# 用True表示含有
soup.find_all(id=True)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


# 传入多个参数
soup.find_all(href=re.compile("elsie"), id='link1')
# [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]


# 在HTML5 中，有些属性需要用attrs属性：
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
data_soup.find_all(attrs={"data-foo": "value"})

# [<div data-foo="value">foo!</div>]
```



#### 3.1.3 根据CSS 的类名（class）搜索

因为`class`是`Python`的保留关键字，BeautifulSoup使用`class_`搜索：

```python
# 搜索css class为 sister的截点
soup.find_all(class_='sister')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


# 搜索class包含多个值的截点：
css_soup = BeautifulSoup('<p class="body strikeout"></p><p class="body"></p><p class="strikeout"></p>')

css_soup.find_all(class_='body')
#[<p class="body strikeout"></p>, <p class="body"></p>]

css_soup.find_all(class_='body strikeout')
#[<p class="body strikeout"></p>]

# 顺序很重要，类名反过来则查不到
css_soup.find_all(class_='strikeout body')
# []

#当然attrs属性获取也是可以的（beautifulSoup老版本没有class_）：
css_soup.find_all(attrs={'class':'body'})
# [<p class="body strikeout"></p>, <p class="body"></p>]

```



#### 3.1.4 字符串（string）

`find_all()`通过字符串参数，可以直接查询HTML中的字符串：

```python

soup.find_all(string="Elsie")
# [u'Elsie']

soup.find_all(string=["Tillie", "Elsie", "Lacie"])
# [u'Elsie', u'Lacie', u'Tillie']

soup.find_all(string=re.compile("Dormouse"))
[u"The Dormouse's story", u"The Dormouse's story"]

def is_the_only_string_within_a_tag(s):
    """Return True if this string is the only child of its parent tag."""
    return (s == s.parent.string)

soup.find_all(string=is_the_only_string_within_a_tag)
# [u"The Dormouse's story", u"The Dormouse's story", u'Elsie', u'Lacie', u'Tillie', u'...']
```

可以看到，`string`主要是匹配文档中的字符，我们可以结合`name`参数获取对应节点：

```python
# 获取文本包含Lacie的a标签节点
soup.find_all('a',string=re.compile('Lacie'))

# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
```



#### 3.1.5 Limit

类似`SQL`中的`limit`，当结果有多条记录时，可以使用`limit`控制返回数量（好像没有SQL中对应的offset属性）：

```python
soup.find_all("a", limit=2)

# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

```



#### 3.1.6 递归（recursive）

一段HTML代码如下：

```html
<div id='aa'>
    <span id='bb'></span>
    <div id='cc'>
        <span id='dd'></span>
    </div>
</div>
```

当我们使用`find_all()`寻找节点或内容时，默认会寻找所有当前节点下所有后代节点，有时我们只希望寻找“儿子”节点，需要设置`recursive=False`：

```python
# 从div节点向下寻找span节点，可以找到2个
soup.div.find_all('span')
# [<span id="bb"></span>, <span id="dd"></span>]



# 从div节点的”儿子中“中寻找span节点，只能找到1个
soup.div.find_all('span',recursive=False)
# [<span id="bb"></span>]

```



### 3.2 CSS选择器

BeautifulSoup也支持通过`select()`方法使用CSS选择器，如：

```python
soup.select("title")
# [<title>The Dormouse's story</title>]

soup.select("p:nth-of-type(3)")
# [<p class="story">...</p>]
```

结合Chome浏览器的赋值CSS选择器功能，可以很快定位到所需内容：

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210729195641.png?x-oss-process=style/wp)







------

参考信息：

* [Beautiful Soup Documentation](https://beautiful-soup-4.readthedocs.io/en/latest/#)

