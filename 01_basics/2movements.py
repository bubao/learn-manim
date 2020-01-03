'''
@Description: 
@Author: bubao
@Date: 2020-01-03 16:28:45
@LastEditors  : bubao
@LastEditTime : 2020-01-03 16:34:07
'''
from manimlib.imports import *


class MoveAlongPath1(Scene):
    def construct(self):
        circle = Circle(radius=4)  # 半径为4的○
        square = Square()  # 正方形
        square.move_to(2 * RIGHT)  # 正方形的起始位置中心点的右边2单位处
        self.add(square)  # 添加正方形
        self.add(circle)  # 添加圆形
        self.play(MoveAlongPath(square, circle),
                  run_time=5.0)  # 运动轨迹正方形绕着圆形转，运行时间5
        self.play(MoveAlongPath(square, circle))  # 再来一次


class MoveAlongPath2(Scene):
    def construct(self):
        circle = Circle(radius=4)
        square = Square()
        square.move_to(2 * RIGHT)
        self.add(square)
        self.play(MoveAlongPath(square, circle), run_time=5.0)
        self.play(MoveAlongPath(square, circle))
