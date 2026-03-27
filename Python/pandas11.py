import pandas as pd

studentdata = [
    [1, "Ali", 89],
    [11, "Ali", 85],
    [13, "Ali", 75]
]

df = pd.DataFrame(studentdata, columns=['stdid', 'name', 'marks'])

# print(df)

# print(df.size)
# print(df.columns)
# df.head()
# df.tail(2)
# df.shape
# df.size
# df.size
# df.dtypes
# df.values
# df.index

# print(df['marks'])
# print(df['name'])

# filtering rows like sql
print(df[df['marks']>80])

df['phone']=[12,33,22]
print(df)

df.insert(4,"malik",90)
print(df)

df.insert(2,"awais",70)
print(df)

df=df.drop(columns=['phone'])
df
print(df)





