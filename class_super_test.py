#-*- coding：utf-8 -*-
class A(object):
    def __init__(self,xing,gender):         #！#1
        self.namea="aaa"                    #！#2
        self.xing = xing                    #！#3
        self.gender = gender                #！#4
         
    def funca(self):
        print("function a : namea-%s,"%self.namea)
  
class B(A):
    def __init__(self,xing,age):            #！#5
        super(B,self).__init__(xing,age)    #！#6（age处应为gender）
        self.nameb="bbb"                    #！#7
        self.namea="ccc"                  #！#8
        ##self.xing = xing.upper()          #！#9
        self.age = age                      #！#10
         
    def funcb(self):
        print("function b : nameb--%s gender--%s" %(self.nameb,self.gender))

b=B('kyl',3)
b.funca()
b.funcb()
print(b.age)