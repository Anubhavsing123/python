#Write a Python program to determine how many elements are in a set without using the built-in len() function.
animals = {"cat", "dog", "bird", "fish"}
c=0
for i in animals:
    if i!=None:
     c+=1
    else:
       break
print(c)
