# Count vowels and consonants in a sentence.
s="Loops are Fun!"
vowels = "aeiou"
v=0
c=0
for i in s:
   if i.isalpha():
      if i in vowels:
         v+=1
      else:
         c+=1
print(v,c,end=" ")