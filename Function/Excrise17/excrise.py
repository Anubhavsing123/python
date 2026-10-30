#Exercise 17. You have a list of tuples representing students and their grades: [("Alice", 88), ("Bob", 75), ("Charlie", 92)]. Use the sorted() function and a lambda to sort this list based on the grades (the second element) in ascending order.
students = [("Alice", 88), ("Bob", 75), ("Charlie", 92)]
sorted_student=sorted(students,key=lambda st:st[1])
print(sorted_student)