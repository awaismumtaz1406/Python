# 1)
list=[2,3,4,45]
for i in list:
 print(i, end="")
 

# 2)
n1={
 "ahmed":23,
 "awai":34,
  "ahmed":23,
 "awai":34
}

n2={
 
  "ahed":23,
 "aai":34,
  "ahmd":23,
 "awai":34
}

n=n1 | n2
nn={**n1,**n2}

print(nn)


# 3 calender
# import calendar
# month=calendar.month(2026,2)
# print(month)

# import calendar
# from turtle import pd
# month=calendar.isleap(2026)
# print(month)


# from datetime import datetime
# time_now = datetime.now().strftime('%H:%M:%S')
# print(f'The time now is {time_now}')

# print(''' \faasigaiu 
#       malirk F
#       \jkF ouegbh''')






# def creater():
#   list=[]
#   i=1
#   while i<=10:
#     list.append(i)
#     i+=1
#     return list
# print(creater())
# import sys
# nm=list(range(1,20))
# print(nm)


# nm = list(range(1, 20))
# print(nm)



# def creater():
#   i=1
#   while i<=10:
#     list.append(i)
#     i+=1
# print(creater())
# x=creater()
# print(next(x))




# list=[2,33,22,11,44,55]
# l=list.sort(reverse=True)
# print(l)




# a=10
# b=5
# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)

# from collections import Counter, counter 
# list1 = ['John','Kelly', 'Peter', 'Moses', 'Peter']
# count_peter = Counter(list1).get("Peter")
# print()


list1 = [[1, 2, 3],[4, 5, 6]]
# l=[]
# for i in list1:
#     for j in i:
#        l.append(j)
# print(l)       




l=[i for j in list1 for i in j]
print(l)


























