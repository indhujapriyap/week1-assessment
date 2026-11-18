class InvalidSalaryError(Exception):
    """Raised when a salary is negative."""
    pass


# Function with default value, *args and **kwargs 
def bonus(salary, rate=0.1, *extras, **options):
    # salary * rate, plus all the extra amounts
    result = salary * rate + sum(extras)

    
    cap = options.get("cap")
    if cap is not None and result > cap:
        result = cap
    return result


#  Classes 
class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")
        self.name = name
        self.salary = salary

    def annual_salary(self):
        # Decision: I treat salary as monthly pay, so yearly = salary * 12
        return self.salary * 12

    def get_details(self):
        return f"{self.name} earns {self.salary} per month"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   
        self.team_size = team_size

    def get_details(self):               
        return f"{self.name} manages {self.team_size} people and earns {self.salary} per month"
# try , except ,finally 
try:
    Employee("Test", -500)
except InvalidSalaryError as error:
    print("Error:", error)
finally:
    print("Transaction finished")

#  Bonus 
print("Bonus 1:", bonus(50000))                          # 5000.0
print("Bonus 2:", bonus(50000, 0.1, 500, 300))           # 5000 + 800 = 5800.0
print("Bonus 3 (capped):", bonus(50000, 0.2, 500, cap=8000))  # 10500 capped to 8000

# Class demo 
emp = Employee("Arun", 30000)
print(emp.get_details(), "| yearly:", emp.annual_salary())
mgr = Manager("Priya", 80000, 5)
print(mgr.get_details())






