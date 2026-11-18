import pandas as pd 
df=pd.read_csv("data/employees_messy.csv")

# ---------- Look at the problems first ----------
print("Rows before cleaning:", len(df))
print("Missing salaries:", df["salary"].isna().sum())
print("Duplicate rows:", df.duplicated().sum())
print("Salary type before:", df["salary"].dtype)

# ---------- Fix 1: remove the repeated row ----------
df = df.drop_duplicates()
print("Rows after removing duplicates:", len(df))

# ---------- Fix 2: fill the empty salaries with the median ----------
median_salary = df["salary"].median()
print("Median salary:", median_salary)
df["salary"] = df["salary"].fillna(median_salary)

# ---------- Fix 3: make the salary a whole number ----------
df["salary"] = df["salary"].astype(int)
print("Salary type after:", df["salary"].dtype)

# ---------- Save and show the clean table ----------
df.to_csv("data/employees_clean.csv", index=False)
print(df)