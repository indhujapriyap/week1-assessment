import csv
import json

employees=[]
with open("data/employees.csv",newline="") as file:
    reader=csv.DictReader(file)
    for row in reader:
        row['id'] = int(row["id"])
        row['salary']=int(row['salary'])
        employees.append(row)
high_earners=[e for e in employees if e['salary'] > 50000]

with open("data/employees.json","w") as file:
    json.dump(employees,file,indent=4)

with open("data/high_earners","w",newline="") as file:
    writer=csv.DictWriter(file,fieldnames=["id","name","department","salary","city"])
    writer.writeheader()
    writer.writerows(high_earners)
    print(f"Rows Read: {len(employees)},high earners:{len(high_earners)}")