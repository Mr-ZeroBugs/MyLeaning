import pandas as pd

data = {'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]}  #outlier is 100
df = pd.DataFrame(data)

# calculate Q1, Q3 and IQR
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1

# กำหนดค่าต่ำสุดและค่าสูงสุด
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print("low", lower_bound, "upper", upper_bound)
# ตรวจสอบว่าแต่ละค่าตรงตามเงื่อนไข
outliers = df[(df['value'] < lower_bound) | (df['value'] > upper_bound)]

print("Outliers:")
print(outliers)

# del outliers
df_no_outliers = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]
print("\nDataFrame after removing outliers:")
print(df_no_outliers)

#replace
mean_value = df['value'].mean()
df['value'] = df['value'].where((df['value'] >= lower_bound) & (df['value'] <= upper_bound), mean_value)

print("\nDataFrame after replacing outliers with mean:")
print(df)
