import pandas as pd

list = {
    'name' : [12, 12, 11],
    'age' : [12, 12, 12]
}

df = pd.DataFrame(list)
print(df)
print(df.duplicated())
print(df.drop_duplicates())