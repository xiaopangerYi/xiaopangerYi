'''
定义一个学生类
'''

class Student():
    #一个空类，pass 代表直接跳过
    pass
#定义一个对象
mingyue = Student()


#定义一个类，学习python学生
class PythonStudent():
    #用None给不缺定值赋值
    name = None
    age = 18
    course = "python"
    def doHomework(self):

        print("I在做作业")
        return None

#实例化
yueyue = PythonStudent()
print(yueyue.age)

#注意成员函数调用没有传递进入参数
yueyue.doHomework()
