sales = [10, 25, 15, 30, 20, 40, 35]
ma=0
for i in range(0,len(sales)-1):
  if sales[i]>sales[i-1] and sales[i]>sales[i+1]:
        ma=max(ma,sales[i])
print(ma)          