# Exercise 37. Display all prime numbers within a range
#m-1 
# for i in range(1,21):
#     if i>1:
#         p=True
#         for n in range(2,i):
#             if i%n==0:
#                 p=False
#                 break
#         if p:
#             print(i,end=" ")

#sqrt
# for num in range(1,21):
#     if num>1:
#         is_prime=True
#         for i in range(2,int(num**0.5)+1):
#             if num%i==0:
#                 is_prime=False
#                 break
#         if is_prime:
#             print(num, end=" ")
#sev
prime=[False]*21
prime[0]=True
prime[1]=True
for num in range(2,int(20**0.5)+1):
    if not prime[num]:
        for j in range(num*num,21,num):
            prime[j]=True
for num in range(1,21):
    if  not prime[num]:
        print(num,end=" ")
   


