#Exercise 19. Remove Empty Strings from a List of Strings
l=["Mike", "", "Emma", "Kelly", "", "Brad"]
l=[x for x in l if x!=""]
print(l)