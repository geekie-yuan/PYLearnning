import math
import unittest
#打印
# str1="Hello World!"
# print(f"str1的内容为：{str1}")
#
# #输入
# user_name=input()
# user_type=input()
# print("你好：%s 您是尊贵的：%s" %(user_name,user_type))

# #布尔类型
# bool_1=1>2
# bool_2=2>1
# print(f"bool_1的类型为：{bool_1}"'\n'f"bool_2的类型为：{bool_2}")

#多条件判断
# num1=int(input("请输入一个数字: "))
# if num1>0:
#     print("输入大于0")
# elif num1<0:
#     print("输入小于0")
# else:
#     print("等于0")

#列表
shoping_list=["显示器","鼠标"]   #添加列表
shoping_list.append("U盘")
shoping_list.append("硬盘")
shoping_list.extend(['test1','test2'])
print(shoping_list)
shoping_list.remove("test1")    #删除列表
print(f"{shoping_list},\n")
del shoping_list[4]
print(shoping_list)
shoping_list.insert(1,"显卡")
print(f"{shoping_list},\n")
shoping_list.sort() #排序
print(f"{shoping_list},\n")
for list in shoping_list[:2]:   #遍历
    print(list)
print('\n')
unimportant_shoping_list = shoping_list[:]    #复制
print(unimportant_shoping_list)

# #字典
# contacts={"小明":"123",
#           ("张伟",23):"456",
#           ("张伟",34):"789"}
# print(contacts["小明"])
# print(contacts["张伟",23])

# # Fot循环
# temputure_list=[36.1,36.6,36.8,37,36.2,37.4,38]
# for temperture in temputure_list:
#     if temperture>37:
#         print(temperture)
#         print("完蛋")

# while循环
# sum=0
# count=0
# while (num :=input("请输入数字，按q结束:"))!='q': #:= 是海象运算符（walrus operator），它允许在表达式内部进行赋值操作。
#     try:    #try 语句块中的代码会被尝试执行。如果执行过程中发生了异常（错误），程序会跳到 except 块中执行相应的错误处理代码
#         num=float(num)
#         sum+=num
#         count+=1
#         result = sum / count
#     except ValueError:
#         print("输入了不合理的数字")
#     except ZeroDivisionError:   # 当尝试除以零时会引发 ZeroDivisionError 异常
#         print("除数不能为零")
#     except Exception as e:   # 捕获所有其他类型的异常
#         print(f"输入错误,错误类型:{e}")
# print(f'平均值为:{result:.2f}')

#函数
# def count_avg():
#     sum = 0
#     count = 0
#     while (num :=input("请输入数字，按q结束:"))!='q': #:= 是海象运算符（walrus operator），它允许在表达式内部进行赋值操作。
#         try:    #try 语句块中的代码会被尝试执行。如果执行过程中发生了异常（错误），程序会跳到 except 块中执行相应的错误处理代码
#             num=float(num)
#             sum+=num
#             count+=1
#             result = sum / count
#         except ZeroDivisionError:   # 当尝试除以零时会引发 ZeroDivisionError 异常
#             print("除数不能为零")
#         except Exception as e:   # 捕获所有其他类型的异常
#             print(f"输入错误,错误类型:{e}")
#     return result
# a=float(count_avg())
# print(f"{a:.2f}")

#面向对象的编程
# class Student:
#     def __init__(self,name,student_id):
#         self.name=name
#         self.student_id=student_id
#         self.grades={"语文":0,"数学":0,"英语":0}
#     def set_grade(self,course,grade):
#         if course in self.grades:
#             self.grades[course]=grade
#     def print_grades(self):
#         print(f"学生{self.name}(学号:{self.student_id})的成绩为：")
#         for course in self.grades:
#             print(f"{course}:{self.grades[course]}分")
# chen=Student("小陈","1234")
# chen.set_grade("语文",92)
# chen.set_grade("数学",98)
# chen.set_grade("英语",95)
# chen.print_grades()

#继承
# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def print_info(self):
#         print(f"员工名字:{self.name},工号:{self.id}")
#
# class FullTimeEmployee(Employee):
#     def __init__(self,name,id,monthly_salary):
#         super().__init__(name,id)
#         self.monthly_salary=monthly_salary
#     def calculate_monthly_pay(self):
#         return self.monthly_salary
# class PartTimeEmployee(Employee):
#     def __init__(self,name,id,daily_salary,work_days):
#         super().__init__(name,id)
#         self.daily_salary=daily_salary
#         self.work_days=work_days
#     def calculate_monthly_pay(self):
#         return self.daily_salary*self.work_days
# zhangsan=FullTimeEmployee("张三","1001",6000)
# lisi=PartTimeEmployee("李四","1002",230,15)
# zhangsan.print_info()
# lisi.print_info()
# print(zhangsan.calculate_monthly_pay())
# print((lisi.calculate_monthly_pay()))

#读写文件
# f=open("./data.txt","r")  #r只读 w写入 a追加 r+读写
# content=f.read()
# print(content)
# f.close()

# with open("./data.txt","a",encoding="utf-8") as f: #不需要fclose
#     f.write("HELLO WORLD4")

#测试
# class ShoppingList:
#     def __init__(self, shopping_list):
#         self.shopping_list = shopping_list
#     def get_item_count(self):
#         return len(self.shopping_list)
#     def get_total_price(self):
#         total_price = 0
#         for price in self.shopping_list.values():
#             total_price += price
#         return total_price
