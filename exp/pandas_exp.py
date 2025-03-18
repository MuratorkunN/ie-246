import pandas as pd
import numpy as np

nest_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

columnname = ["col0", "col1", "col2"]
rowname = ["row0", "row1", "row2"]

df = pd.DataFrame(nest_list,columns=columnname, index=rowname)
print(df)

row0 = df.iloc[0]
print(row0)

row1 = df.loc["row1"]
print(row1)

row01 = df.iloc[0:2]
print (row01)

col = df["col0"]
print (col)

cols = df[["col1", "col2"]]
print(cols)

element = df.iloc[0, 0]
print(element)
element = df.loc["row1", "col1"]
print(element)

df.loc["newrow"] = [0,0,0]
df["newcol"] = [0,0,0,0]
print(df)

df = df.drop(["newcol"], axis = 1)
print(df)







