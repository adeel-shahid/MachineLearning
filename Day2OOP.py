def printval(args):
    print(args)


printval("Hello Sir")


################################################################
# ObjectOreintedPrograming

# class Student:
#
#     #Constructor
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#
# s1 = Student("Usama",32)
# print("Name of Student: ",s1.name,"\nAge Of Student: ",s1.age)
######################################################################
# Task1
# class Bank:
#
#     def __init__(self, accno, holder, amt, name):
#         self.accno = accno
#         self.holder = holder
#         self.amt = amt
#         self.name = name
#
#     def deposit(self, amnt):
#         self.amt = self.amt + amnt
#
#     def withDraw(self, amnt):
#         if amnt < self.amt:
#             self.amt = self.amt - amnt
#         else:
#             print("Not Enough Balance in Account")
#
#     def ShowBalance(self):
#         print(f'Your Account Balance is {self.amt}')
#
#     def Transfer(self,bAccount,amnt):
#         self.withDraw(amnt)
#         bAccount.deposit(amnt)
#
#
# myAccount = Bank(123, 'Adeel', 12000, 'Shahid')
# myAccount.deposit(100000)
# myAccount.ShowBalance()
# myAccount.withDraw(200)
# myAccount.ShowBalance()
# AccountTrans = Bank(432, 'Haris', 12000, 'Harry')
# myAccount.Transfer(AccountTrans,50000)
# myAccount.ShowBalance()
# AccountTrans.ShowBalance()

#####################################################################
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def Display(self):
#         print("Name = ", self.name, "\nAge = ", self.age)
#
#
# class Student(Person):
#
#     def __init__(self, rollnum, name, age):
#         super().__init__(name, age)
#         self.rollnum = rollnum
#
#     def Display(self):
#         super().Display()
#         print("RollNum = ", self.rollnum)
#
#
# class Employee(Person):
#
#     def __init__(self, name, age, EmpNo, Department):
#         super().__init__(name, age)
#         self.EmpNo = EmpNo
#         self.Department = Department
#
#     def Display(self):
#         super().Display()
#         print("EmpNo = ", self.EmpNo, "Department", self.Department)
#
#
# e1 = Employee('Sir Hassan', 56, 123, 'ManuFactoring')
# s1 = Student(3593, 'Adeel', 23)
#
# print("\nStudent is:")
# s1.Display()
#
# print("\nEmployee is:")
# e1.Display()
#######################################################3333
#matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
# x_data = np.array(['UnEducated','Matric','Intermediate','Above'])
# y_data = np.array([52,45,4,2])
# plt.bar(x_data,y_data)
# plt.xlabel('Level')
# plt.ylabel('Percentage')
# plt.grid()
# plt.show()
# # plt.pie(y_data)
# # plt.legend(['UnEducated','Matric','Intermediate','Above'])
# myexplode = [0.2, 0, 0, 0]
# plt.pie(y_data, labels = ['UnEducated','Matric','Intermediate','Above'],explode=[0, 0, 0, 0.5],autopct='%1.1f%%')
# plt.show()
###############################################################################################################################
#Task

# import matplotlib.pyplot as plt
# import numpy as np
# pakscore = np.array([5,35,65,85,400])
# overs = np.array([1,10,15,20,25])
# indscore = np.array([3,50,40,90,350])
# plt.xlabel('Overs')
# plt.ylabel('Scores')
# plt.plot(overs,pakscore,'g',label = 'Pakistan')
# plt.plot(overs,indscore,'o--',label = 'India')
# plt.legend()
# plt.grid()
# plt.show()
#################################################################
#plt.subplot(rows,columns,position)
#Task
# import matplotlib.pyplot as plt
# import numpy as np
# pakscore = np.array([5,35,65,85,400])
# overs = np.array([1,10,15,20,25])
# indscore = np.array([3,50,40,90,350])
# plt.xlabel('Overs')
# plt.ylabel('Scores')
# plt.subplot(1,2,1)
# plt.plot(overs,pakscore,'g',label = 'Pakistan')
# plt.grid()
# plt.legend()
# plt.subplot(1,2,2)
# plt.plot(overs,indscore,'o--',label = 'India')
# plt.legend()
# plt.grid()
# plt.show()
##############################################################################33
#Pandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('IndiaCovidCasesByStateUT.csv')
# print(df.head(10))
# print(df.tail())
# print(df.shape)

state = np.array(df.get('State/UTs'))
case = np.array(df.get('Total Cases'))

plt.bar(state,case)
plt.xlabel('States')
plt.ylabel('Cases')
plt.xticks(rotation=70,ha='right')
plt.cool()
pr = plt.bar(state,case)
pr[-1].set_color('red')
plt.title('Covid-19 cases in  India')
plt.show()
##############################################################
#install flask
