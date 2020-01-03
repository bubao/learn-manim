'''
@Description: 
@Author: bubao
@Date: 2020-01-03 16:17:30
@LastEditors  : bubao
@LastEditTime : 2020-01-03 16:27:59
'''
from manimlib.imports import *


class ChangeShape(Scene):
    def construct(self):
        circle = Circle()  # 圆圈
        square = Square()  # 正方形
        self.play(Transform(circle, square))  # 圈转换成正方形 circle变成正方形
        self.wait(1)  # 等一秒
        new_circle = Circle()  # 创建一个新的圈
        self.play(Transform(circle, new_circle))  # 从原来转换的圈->正方形->圈
        self.wait(1)


class Surround(Scene):
    def construct(self):
        circle = Circle()  # 圆圈
        square = Square()  # 正方形
        circle.surround(square)  # 圈包含正方形
        self.play(FadeIn(square))  # 渐显正方形
        self.play(GrowFromCenter(circle))  # 居中生成
        self.wait(1)
