#Create a function that takes a list of numbers as input and returns the largest item from that list without using the built-in max() function (to practice manual logic).

def find_largest(li):
    l=li[0]
    for i in li:
        if i>l:
            l=i
    return l
x=[4, 6, 8, 24, 12, 2]
print(find_largest(x))