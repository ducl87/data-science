# Manim操作（持续完善中）

[toc]

## 快速入门

文件目录结构：

```
project/
└─scene.py
```

代码：

```python
from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
```



使用命令行`manim -pql scene.py SquareToCircle`即可得到下列视频。

<video  src="https://docs.manim.community/en/stable/tutorials/SquareToCircle-1.mp4" />



常见命令行：`mainm -参数 文件名.py 类名`

```shell
manim -pql scene.py SquareToCircle
```

* -ql: 低分辨率，其他的还有`-qm,-qh,-qk`对应中等、高、4K质量
* -p：预览
* -f：完成后打开文件所在位置
* -i：生成GIF动画



## manim的主要构成

### 三个主要概念

* 数学对象：`mobject`，如`Circle`,`Arrow`,`Rectangle`等基本对象，或者`Axes`,`FunctionGraph`,`BarChart`等复杂对象
* 动画：`animation`
* 场景：`scene`

### Mobjects

#### 创建并且展示mobjects

```python
from manim import *

class CreatingMobjects(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)
```

如上面代码所示，一般我们会将所有的`manim`代码放在类的构造函数`construct`内，在没有引入动画前，使用：

1. `add()`显示一个`mobject`;
2. `remove()`移除一个`mobject`.

效果如下：

<video src="https://docs.manim.community/en/stable/tutorials/CreatingMobjects-1.mp4">
</video>



#### mobjects的位置

对象在刚创建的时候，会默认放在画面中央，使用以下方法调整对象的位置：

`shift()`方法：

```python
from manim import *

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)
```



![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210907151446.png?x-oss-process=style/wp)



`shift()`接受的参数有`LEFT,RIGHT,UP,DOWN,ORGIN`。

除了`shift()`，还有`move_to(),next_to(),align_to()`方法可以控制位置：

```python
class OtherPlacingObject(Scene):
    def construct(self):
        circle  = Circle()
        triangle = Triangle()
        square = Square()
        # 正方形向左移动3个单位
        square.move_to(LEFT*3)
        # 圆与正方形左对齐
        circle.align_to(square,LEFT)
        # 三角形放在正方形的下面
        triangle.next_to(square,UP)
        self.add(square,circle,triangle)
        self.wait(1)
```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210907152208.png?x-oss-process=style/wp)

可以看到`move_to()`使用绝对单位，而`align_to(),next_to()`使用相对单位。

#### mobjects的样式

* `set_stroke()`设置边框风格
* `set_fill()`设置内部风格

```python
class MobjectsStyle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Square()

        circle.move_to(LEFT)
        square.move_to(UP)
        triangle.move_to(RIGHT)

        # 圆设置边框
        circle.set_stroke(
            color=GREEN,
            width=30
        )
        # 正方形设置内部
        square.set_fill(
            color = YELLOW,
            opacity= 1
        )
        # 三角形设置样式
        triangle.set_fill(
            color = PINK,
            opacity=0.5
        )
        self.add(circle,square,triangle)
        self.wait(1)
```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210907155933.png?x-oss-process=style/wp)



需要注意`add()`可以控制`mobject`的放置顺序。

### Animation

`play()`是动画的核心函数：

```python
class SimpleAnimation(Scene):
    def construct(self):
        square = Square()

        # 展示
        self.add(square)
        # 淡入
        self.play(FadeIn(square))
        # 旋转
        self.play(Rotate(square,PI/4))
        # 淡出
        self.play(FadeOut(square))

        self.wait(1)
```

<video src="https://docs.manim.community/en/stable/tutorials/SomeAnimations-1.mp4">

</video>



#### 动画方法

只要可以修改的`mobject`属性，都可以用作动画，只要将原来类似`object.set_property()`的函数修改为`object.animate.set_property()`即可产生动画：

```python
from manim import *

class AnimateExample(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        # animate the change of color
        self.play(square.animate.set_fill(WHITE))
        self.wait(1)

        # animate the change of position and the rotation at the same time
        self.play(square.animate.shift(UP).rotate(PI / 3))
        self.wait(1)
```



<video src="https://docs.manim.community/en/stable/tutorials/AnimateExample-2.mp4">

</video>

#### 动画运行时间

`play()`默认时间为1秒，可以通过`run_time`参数设置时间：

```python
from manim import *

class RunTime(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.play(square.animate.shift(UP), run_time=3)
        self.wait(1)
```



#### 使用mobject的坐标点

mobjects图形边缘由点构成，可以通过`get_center(),get_top(),get_start()`方法获取这些点。

#### 不同mobject之间的转换

使用`Transform(m1,m2)`方法将m1转换成m2：

```python
from manim import *

class ExampleTransform(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1 = Square().set_color(RED)
        m2 = Rectangle().set_color(RED).rotate(0.2)
        self.play(Transform(m1,m2))
```

<video src="https://docs.manim.community/en/stable/tutorials/ExampleTransform-1.mp4">

### Scene

场景（Scene）：每一个mobject，每一个动画都在Scene的构造函数内。



## 使用文字

### 简单的文字

#### 入门

使用`Text()`类在视频中加载简单的文字：

```python
class TextDemo(Scene):
    def construct(self):
        text = Text("你好数学",font_size = 144)
        self.add(text)
```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/imgTextDemo_ManimCE_v0.10.0.png?x-oss-process=style/wp)



#### 字体

查看系统已经安装的字体：

```python
>>> import manimpango
>>> manimpango.list_fonts()
[...]

```

设置字体：

```python
class FontsExample(Scene):
    def construct(self):
        ft = Text("圆体字样本", font="Yuanti SC",font_size=144)
        self.add(ft)
```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/imgFontsExample_ManimCE_v0.10.0.png?x-oss-process=style/wp)



#### 风格

* `Slant`: `NORMAL,ITALIC(Roman Style),OBLIQUE(Italic Style)`
* `weight`:使用`manimpango.Weight`查看所有的weight

```python
class FontStyleDemo(Scene):
    def construct(self):
        text = Text("宋体斜体", font="Songti SC",font_size=144,slant = ITALIC)
        self.add(text)
```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/imgFontStyleDemo_ManimCE_v0.10.0.png?x-oss-process=style/wp)



```python
class DifferentWeight(Scene):
    def construct(self):
        

        g = VGroup()
        weight_list = dict(sorted({weight: manimpango.Weight(weight).value for weight in manimpango.Weight}.items(), key=lambda x: x[1]))
        for weight in weight_list:
            g += Text(weight.name, weight=weight.name, font="Open Sans")
        self.add(g.arrange(DOWN).scale(0.5))
```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210907202236.png?x-oss-process=style/wp)

#### 颜色

使用`color`属性，可以快速设置颜色：

```python
class ColorFont(Scene):
    def construct(self):
        text = Text(f"红色的字",color=RED,font_size=144)
        self.add(text)
```



![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/imgColorFont_ManimCE_v0.10.0.png?x-oss-process=style/wp)



也可以使用`t2c`工具渲染颜色：

* 使用list形式传参，选择区间范围；
* 匹配模式，寻找特定字符渲染。

```python
class T2cDemo(Scene) :
    def construct(self):
        text_blue = Text("我是蓝色的字",t2c={'[2:4]':BLUE})
        text_red = Text("我是红色的字",t2c={'红色':RED}).next_to(text_blue,DOWN)
        self.add(text_blue,text_red)

```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/imgT2cDemo_ManimCE_v0.10.0.png?x-oss-process=style/wp)

#### 渐变

```python
class GradientExample(Scene):
    def construct(self):
        text = Text("渐变字体",gradient=(RED,PINK,GREEN),font_size=96)

        self.add(text)

```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/imgGradientExample_ManimCE_v0.10.0.png?x-oss-process=style/wp)

类似`t2c`,可以使用`t2g`指定那些字符渐变：

```python
class t2gExample(Scene):
    def construct(self):
        t2gindices = Text(
            'Hello',
            t2g={
                '[1:-1]': (RED,GREEN),
            },
        ).move_to(LEFT)
        t2gwords = Text(
            'World',
            t2g={
                'World':(RED,BLUE),
            },
        ).next_to(t2gindices, RIGHT)
        self.add(t2gindices, t2gwords)
```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210907203743.png?x-oss-process=style/wp)

#### 行距

```python
class LineSpacing(Scene):
    def construct(self):
        a = Text("单倍\n行距", line_spacing=1).move_to(LEFT)
        b = Text("4倍\n行距", line_spacing=4).next_to(a,RIGHT)
        self.add(a,b)

```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/imgLineSpacing_ManimCE_v0.10.0.png?x-oss-process=style/wp)

#### 遍历文字

```python
class IterateColor(Scene):
    def construct(self):
        text = Text("遍历这个文字", font_size=96)
        for letter in text:
            letter.set_color(random_bright_color())
        self.add(text)
```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/imgIterateColor_ManimCE_v0.10.0.png?x-oss-process=style/wp)

#### MarkupText标记文字

也可以使用`MarkupText()`使用标记语言形式的文本：

```python
class MarkupExample(Scene):
    def construct(self):
        text = MarkupText(f'<span foreground="blue" size="x-large">Blue text</span> is <i>cool</i>!"')

        self.add(text)
```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210907194522.png?x-oss-process=style/wp)

更多规则参见：https://docs.gtk.org/Pango/pango_markup.html#pango-markup



### LaTeX文字

#### Tex,MathTex

```python
class SimpleTex(Scene):
    def construct(self):
        text = Tex(r"$f(x)=\frac{3}{4}x+x^2$",font_size=144).shift(UP)
        text_1 = MathTex(r"f(x)=\frac{3}{4}x+x^2",font_size=144).next_to(text,DOWN)
        self.add(text,text_1)
```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/imgS1impleTex_ManimCE_v0.10.0.png?x-oss-process=style/wp)

需要注意，使用Tex时需要加`$ $`符号。

Text和MathTex也支持`color`属性（其他属性暂不支持），调节字体颜色。

```python
class SimpleTex(Scene):
    def construct(self):
        text = Tex(r"$f(x)=\frac{3}{4}x+x^2$",font_size=144,color=BLUE).shift(UP)
        text_1 = MathTex(r"f(x)=\frac{3}{4}x+x^2",font_size=144,color=PINK).next_to(text,DOWN)
        self.add(text,text_1)
```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/imgSimpleTex_ManimCE_v0.10.02.png?x-oss-process=style/wp)



#### 截取字符串和子部

Tex支持分段传入字符，并且使用索引获取对应部分，如`tex[0]`，下面这个例子使用`set_color_by_tex()`搜索对应字符串上色。

```python
class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex('Hello', r'$\bigstar$', r'\LaTeX', font_size=144)
        tex[0].set_color(PINK)
        tex.set_color_by_tex('igsta', RED)
        self.add(tex)

```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/imgLaTeXSubstrings_ManimCE_v0.10.0.png?x-oss-process=style/wp)

需要注意，`set_color_by_tex`会上色包含字符的整个字符（而不是仅仅被搜索的字符）：

```python
class IncorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.add(equation)

```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210908095808.png?x-oss-process=style/wp)

可以看到，虽然搜索`x`，但是整个公式都上色了。

如果需要仅对`x`部分上色，则需要使用`substrings_to_isolate`：

```python
class SubstringDemo(Scene):
    def construct(self):
        text = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x"
        )
        text.set_color_by_tex("x",RED)
        self.add(text)
```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/imgSubstringDemo_ManimCE_v0.10.0.png?x-oss-process=style/wp)



#### 自定义截取字符串

MathTex使用`{{strings}}`格式包装字符串，会将整个字符串分割成`list`，方便使用索引方式进行调用：

```python
class SubstringDemo(Scene):
    def construct(self):
        text = MathTex(r"{{ a^2 }} + {{ b^2 }} = {{ c^2 }}")
        text[0].set_color(RED)
        text[2].set_color(BLUE)
        text[4].set_color(PINK)
        self.add(text)
```



![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img11SubstringDemo_ManimCE_v0.10.0.png?x-oss-process=style/wp)



#### LaTeX字体

Tex和MathTex使用`tex_template`可以使用不同字体，字体列表参见[TexFontTemplates](https://docs.manim.community/en/stable/reference/manim.utils.tex_templates.TexFontTemplates.html#manim.utils.tex_templates.TexFontTemplates) ：

```python
from manim import *

class LaTeXMathFonts(Scene):
    def construct(self):
        tex = Tex(r'$x^2 + y^2 = z^2$', tex_template=TexFontTemplates.french_cursive, font_size=144)
        self.add(tex)
```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210908104315.png?x-oss-process=style/wp)



#### 中文渲染

使用[TexTemplateLibrary](https://docs.manim.community/en/stable/reference/manim.utils.tex_templates.TexTemplateLibrary.html#manim.utils.tex_templates.TexTemplateLibrary)中的模板可以渲染中文字体（默认不支持），为了渲染中文字体，需要提前安装`ctex`。

```python
class LaTeXTemplateLibrary(Scene):
    def construct(self):
        tex = Tex('你好，恩培！f(x)=2x', tex_template=TexTemplateLibrary.ctex, font_size=100)
        self.add(tex)
```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/imgLaTeXTemplateLibrary_ManimCE_v0.10.0.png?x-oss-process=style/wp)



#### 对齐

```python
class LaTeXAlignEnvironment(Scene):
    def construct(self):
        tex = MathTex(r'f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6', font_size=96)
        self.add(tex)        
```

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/imgLaTeXAlignEnvironment_ManimCE_v0.10.0.png?x-oss-process=style/wp)





## 配置

