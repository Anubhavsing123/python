#Exercise 22. Concatenate Two Lists Index-wise
L1=["Py", "is", "awes"]
L2= ["thon", " ", "ome"]
l=[i+j for i,j in zip(L1,L2)]
print(l)