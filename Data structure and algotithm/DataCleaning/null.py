import pandas as pd

data = {
    "testY1" : [1, 2, 3, None, None],
    "testY2" : [1, 2, 3, 4, 5]
}
dfTest = pd.DataFrame(data)
#check null
print((dfTest.isna()).sum())

#remove rows that contain null
df = pd.read_csv('idk')
new_df = df.dropna()
df.dropna(inplace=True)

#replace rows that contain null
newvalue = df.mean()
df.fillna(newvalue, inplace = True) 

#or only specific column
new2 = df["Calories"].mean()
df["Calories"].fillna(newvalue, inplace = True) 

