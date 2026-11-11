# Exercise 18. Read a file and store its content in a list
fruit_list = ["Apple", "Banana", "Cherry", "Date"]
with open("txt.txt","w") as f:
    for i in fruit_list:
        f.write(i+"\n")
print("File 'fruits.txt' has been created successfully.")