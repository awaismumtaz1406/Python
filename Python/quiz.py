# sales = [10, 25, 15, 30, 20, 40, 35]
# ma=0
# for i in range(0,len(sales)-1):
#   if sales[i]>sales[i-1] and sales[i]>sales[i+1]:
#         ma=max(ma,sales[i])
# print(ma)          




# nums = [1, 2, 3, 2, 4, 2, 5]
# print(nums.count(2))


# temps = [30, 32, 31, 29, 35, 36, 34]
# res = []
# for i in range(0,len(temps)-3):
#       ans=(temps[i]+temps[i+1]+temps[i+2])/3
# res.append(ans)

# print(res)

# cart = [101, 102, 101, 103, 102]
# unique = []
# for i in range(0, len(cart)):
#       if cart[i] not in unique:
#              unique.append(cart[i])

# print(unique)             



tuple=((1,10), (2,20), (3,30),(4,40),(5,50),(8,60), (9,70))
# for i in range(0,len(tuple)-1):
high=max(tuple,a=lambda x:x[1])
print(high)