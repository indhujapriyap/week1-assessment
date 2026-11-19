import pandas as pd

df = pd.read_csv("data/employees.csv")

print("\n---First rows---")
print(df.head())

print("\n---info()---")
df.info()

print("\n---describe()---")
print(df.describe())

print("\n----- loc: rows 0 to 2, columns name and salary -----")
print(df.loc[0:2, ["name", "salary"]])

print("\n--iloc: rows 0 to 1, columns 0 to 2--")
print(df.iloc[0:2, 0:3])

print("\n--Filter: salary above 50000---")
print(df[df["salary"] > 50000])