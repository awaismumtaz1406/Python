import pandas as pd

studentdata = [
    [1, "Ali", 89],
    [11, "Ali", 85],
    [13, "Ali", 75]
]

df = pd.DataFrame(studentdata, columns=['stdid', 'name', 'marks'])

print(df)









