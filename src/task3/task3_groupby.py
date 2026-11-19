import pandas as pd

employees = pd.read_csv("data/employees_clean.csv")
departments = pd.read_csv("data/departments.csv")

summary = employees.groupby("department").agg(
    headcount=("id", "count"),
    avg_salary=("salary", "mean"),
    max_salary=("salary", "max"),
)
summary["avg_salary"] = summary["avg_salary"].round(2)

print(summary)

parts = []
for dept in ["Sales", "HR", "IT", "Finance"]:
    parts.append(f"{dept} {summary.loc[dept, 'headcount']}")
print("Headcount:", " - ".join(parts))

print("\n Merging")



inner = pd.merge(employees, departments, on="department", how="inner")
left = pd.merge(employees, departments, on="department", how="left")
outer = pd.merge(employees, departments, on="department", how="outer")

print("Inner join rows:", len(inner))
print("Left join rows:", len(left))
print("Outer join rows:", len(outer))

no_employees = outer[outer["name"].isna()]
print("Outer join: department with no employees listed:", list(no_employees["department"]))