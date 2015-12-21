# -*-coding: utf-8 -*-

class Human(object):
    laugh='哈哈'
    # Man_genter='男'
    def __init__(self):
        print self.laugh+'初始化'
    def __init__(self,input_gender):
        self.Man_genter=input_gender
    def Show_laugh(self):
        print self.laugh
    def laugh_100th(self):
        for i in range(2):
            self.Show_laugh()
class superList(list):
    def __sub__(self,b):
        a=self[:]
        b=b[:]
        while len(b)>0:
            element_b=b.pop()
            if element_b in a:
                a.remove(element_b)
        return a

liu=Human('女')
print liu.Man_genter
mm=Human('男')
print mm.Man_genter
mm.laugh_100th()
print superList([1,2,3])-superList([3,4])