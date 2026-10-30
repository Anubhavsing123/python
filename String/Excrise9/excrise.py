#Practice Problem: 
# Write a program to check if two strings are balanced. 
# For example, strings s1 and s2 are balanced if all the characters in s1 are present in s2.
#  The character’s position doesn’t matter.
s1 = "yn"
s2 = "PyNative"
def check_tr(s1,s2):
   if s1 in s2.lower():
     return True
   else:
      return False
s=check_tr(s1,s2)
print(s)
#m-2
def string_balance_check(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
            break
    return flag

s1 = "yn"
s2 = "PyNative"
print("Is s1 and s2 balanced:", string_balance_check(s1, s2))

s1 = "ynf"
s2 = "PyNative"
print("Is s1 and s2 balanced:", string_balance_check(s1, s2))