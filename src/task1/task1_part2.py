#  Data
employees = [
    {"id": 1, "name": "Arun", "department": "Sales", "salary": 30000, "city": "Chennai"},
    {"id": 2, "name": "Priya", "department": "HR", "salary": 45000, "city": "Chennai"},
    {"id": 3, "name": "Rahul", "department": "IT", "salary": 60000, "city": "Bangalore"},
    {"id": 4, "name": "Divya", "department": "IT", "salary": 75000, "city": "Chennai"},
    {"id": 5, "name": "Karthik", "department": "Finance", "salary": 90000, "city": "Mumbai"},
    {"id": 6, "name": "Meena", "department": "Sales", "salary": 52000, "city": "Bangalore"},
    {"id": 7, "name": "Suresh", "department": "IT", "salary": 68000, "city": "Chennai"},
    {"id": 8, "name": "Anitha", "department": "HR", "salary": 48000, "city": "Mumbai"},
]

#  List comprehension: salary above 50000
above_50k = [e["name"] for e in employees if e["salary"] > 50000]
print("Above 50000:", above_50k)

#  map + lambda: add 10% raise
raised = list(map(lambda e: round(e["salary"] * 1.1), employees))
print("Salaries after 10% raise:", raised)

#  filter: keep Chennai employees 
chennai_employees = list(filter(lambda e: e["city"] == "Chennai", employees))
print("\nchennai_employees:",chennai_employees)
print("Chennai:", [e["name"] for e in chennai_employees])

# for loop with continue and break 
salaries = [30000, 0, 45000, 60000, 90000, 52000]   
for s in salaries:
    if s == 0:
        print("Skipping salary 0")
        continue                 
    print("Checking salary:", s)
    if s > 85000:
        print("First salary above 85000 found:", s)
        break                   