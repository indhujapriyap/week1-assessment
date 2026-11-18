import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/employees_clean.csv")
avg_salary = df.groupby("department")["salary"].mean()

print("\n chart 1 : bar")
plt.figure(figsize=(7, 5))
plt.bar(avg_salary.index, avg_salary.values, color="steelblue", label="Average salary")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average salary (Rs)")
plt.legend()
plt.savefig("reports/1_bar_avg_salary.png")
plt.close()

print("\nChart 2: histogram")
plt.figure(figsize=(7, 5))
plt.hist(df["salary"], bins=5, color="seagreen", edgecolor="black", label="Employees")
plt.title("Salary Distribution")
plt.xlabel("Salary (Rs)")
plt.ylabel("Number of employees")
plt.legend()
plt.savefig("reports/2_histogram_salary.png")
plt.close()

print("\nChart 3: scatter")
plt.figure(figsize=(7, 5))
for dept, group in df.groupby("department"):
    plt.scatter(group["id"], group["salary"], s=80, label=dept)
plt.title("Salary of Each Employee by Department")
plt.xlabel("Employee id")
plt.ylabel("Salary (Rs)")
plt.legend()
plt.savefig("reports/3_scatter_salary.png")
plt.close()

print("\n chart 4 : line")
plt.figure(figsize=(7, 5))
plt.plot(df["id"], df["salary"], marker="o", color="darkorange", label="Salary")
plt.title("Salary by Employee id")
plt.xlabel("Employee id")
plt.ylabel("Salary (Rs)")
plt.legend()
plt.savefig("reports/4_line_salary.png")
plt.close()

# One sentence of insight per chart
top = df.loc[df["salary"].idxmax()]
insights = [
    f"Bar chart: {avg_salary.idxmax()} has the highest average salary ({avg_salary.max():.0f}) and {avg_salary.idxmin()} the lowest ({avg_salary.min():.0f}).",
    f"Histogram: the median salary is {df['salary'].median():.0f}, with most salaries between 48000 and 75000.",
    f"Scatter: the highest paid employee is {top['name']} from {top['department']} ({top['salary']}).",
    "Line chart: salary does not rise with employee id, so pay depends on role and not on joining order.",
]
with open("reports/insights.txt", "w") as file:
    file.write("\n".join(insights))

for line in insights:
    print(line)
print("4 charts saved in the reports folder")