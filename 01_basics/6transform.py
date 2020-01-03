'''
@Description: 
@Author: bubao
@Date: 2020-01-03 17:15:06
@LastEditors  : bubao
@LastEditTime : 2020-01-03 17:16:09
'''
from manimlib.imports import *


class ChangeShape(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Transform(circle, square))
        new_circle = Circle()
        self.play(Transform(circle, new_circle))
        self.play(Transform(circle, square))
        self.play(Transform(circle, new_circle))
