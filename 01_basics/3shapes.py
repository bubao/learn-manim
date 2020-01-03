'''
@Description: 
@Author: bubao
@Date: 2020-01-03 16:35:25
@LastEditors  : bubao
@LastEditTime : 2020-01-03 16:39:38
'''
from manimlib.imports import *


class Primitives(Scene):

    def construct(self):
        # TODO: put more complicated examples, e.g. parameters, in new example. Keep this one streight forward
        # circle = Circle(
        #     radius=4,
        #     stroke_width=50,
        #     stroke_color='#ffffff',
        #     fill_color='#ff0000',
        #     fill_opacity=1
        # )
        circle = Circle()  # 圆形
        self.play(FadeIn(circle))  # 淡入
        self.play(FadeOut(circle))  # 淡出

        square = Square()  # 正方形
        self.play(FadeIn(square))
        self.play(FadeOut(square))

        rect = Rectangle()  # 长方形
        self.play(FadeIn(rect))
        self.play(FadeOut(rect))
