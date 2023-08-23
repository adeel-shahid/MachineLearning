# print("Hello World")
# a = int(input("Enter a Number:"))
# flag = False
# for i in range(2,a):
#     if i != a and a % i == 0:
#         flag = True
#         break
#     else:
#         flag = False
# if not flag:
#     if a != 0 and a != 1:
#         print("Number is Prime")
#     else:
#         print("Number is not prime")
# else:
#     print("Number is not prime")


###########################################################################
# import random as rd
# roles = 0
# count = 0
# i = 0
#
#
# while count < 10:
#     dice1 = rd.randint(1, 6)
#     dice2 = rd.randint(1, 6)
#     roles += 1
#     if dice2 == 6 or dice1 == 6:
#         count += 1
#     if (dice1 + dice2) >= 10:
#         count += 1
# print(f'roles = {roles} \n Count = {count}')
################################################################################
# students = {
#     '3593': ['Adeel',3.93],
#     '3694': ['Anees',3.08],
#     '3583': ['Abdullah',3.58],
#     '3664': ['Usama',3.00],
#     '3641': ['Haris',4.00],
# }
# cream = []
# for val in students.values():
#     if val[1] >= 3.50:
#         cream.append(val[0])
#
# print("Students with Cream : ",cream)


#########################################################################
# def display(d):
#     for key, value in d.items():
#         print("Key-->", key, ",value-->", value)
#     print("\n")
#
# dict = {
#     'k1':'v1',
#     'k2':'v2',
#     'k3':'v3'
# }
#
#
# display(dict)
# dict['k4'] = 'v4'
# display(dict)
# dict.update({'k4':'v7'})
# display(dict)

###############################################################################
# import math as mth
# dict = {
#     '3593' : ['Adeel',3.93,7],
#     '3594' : ['Aness',0.70,1],
#     '3595' : ['Abdullah',1.12,3],
#     '3596' : ['Usama',3.12,7],
#     '3597' : ['Ahsan',3.12,7],
# }
#
# avggpa = [0.75,1.25,1.75,2.25]
#
# dropdict = []
#
# for key,value in dict.items():
#     if value[1] <= avggpa[mth.ceil((value[2])/2)-1]:
#         dropdict.append(key)
#
# print(dropdict)
####################################################################
# LEAP YEAR OR NOT HACKER RANK Question
def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
        if year % 400 == 0:
            leap = True
    return leap


year = int(input())
print(is_leap(year))