from manim import *
# Screen size
config.pixel_height = 960
config.pixel_width = 540

# 1920/1080
# 3840/2160
config.frame_width = 10
# config.frame_y_radius = 5

# frame rate
# config.frame_rate = 60


# 1、先展示一个坐标上基本的向量，表达方向用转动，表达大小用长短
# 2、最后展示一堆大小方向不同的向量分布在原点周围

class Scene1(Scene):
    def construct(self):
        
        
        # 创建网格
        number_plane = NumberPlane(

            x_range = [-5,5,1],
            y_range = [-10,10,1],
            x_length=10,
            y_length=20,
            background_line_style={
                "stroke_opacity": 0.5
            }
            
        )
        # 解决动画导致的白线不出来的问题
        number_plane_1 = number_plane.copy()

        # 创建动画
        self.play(Create(number_plane),run_time=0.5)
        # 加上白线
        self.add(number_plane_1)


        # 加上向量
        arrow_1 = Arrow(
            start = (0,0,0),
            end = (2,3,0),
            buff=0,
            color =PINK
        )
        arrow_2 = Arrow(
            start = (0,0,0),
            end = (1,1.5,0),
            buff=0,
            color =PINK
        )
        arrow_3 = Arrow(
            start = (0,0,0),
            end = (4,6,0),
            buff=0,
            color =PINK
        )
        # 向量坐标
        arrow_1_text = Matrix([[2],[3]]).next_to(arrow_1,UP)
        # 展示向量运动
        self.play(GrowArrow(arrow_1))
        # 显示向量坐标
        self.play(Create(arrow_1_text),run_time=0.4)

        self.wait(1)
        # 表达有方向：先向左旋转45度，再向右旋转90度
        self.play(Rotate(arrow_1,PI/2,about_point=(0,0,0)),run_time=0.5)
        self.play(Rotate(arrow_1,-PI/2,about_point=(0,0,0)),run_time=0.5)
        self.wait(0.5)
        # 表达大小，伸缩
        self.play(Transform(arrow_1,arrow_2),run_time=0.5)

        self.play(Transform(arrow_1,arrow_3),run_time=0.5)

        arrow_2_text = Matrix([[4],[6]]).next_to(arrow_3,UP)
        self.play(Transform(arrow_1_text,arrow_2_text),run_time=0.5)


# 1、以一批房屋的特征为例，动画将面积、房间数等转化为向量动画
# 3、经过模型进行运算
# 3、输出一个向量

class Scene2(Scene):
    def construct(self):
