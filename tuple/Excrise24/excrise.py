# Problem Statement: Use collections.namedtuple to define an Employee data structure with named fields, create a few instances, and perform a calculation such as finding the highest-paid employee.
from collections import namedtuple
Employee=namedtuple("Employee",["name","department","salary"])
employee=(
    Employee("Alice",   "Engineering", 95000),
    Employee("Bob",     "Marketing",   72000),
    Employee("Charlie", "Engineering", 88000),
)
for emp in employee:
    print(f"{emp.name} works in {emp.department} and earns ${emp.salary:,}")

top = max(employee, key=lambda e: e.salary)
print(f"Highest paid: {top.name} (${top.salary:,})")