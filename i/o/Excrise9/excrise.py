# Exercise 9: Display right-aligned output
# word = input("Enter a word: ")
# version = input("Enter a version number: ")

# # Right-align the word in 20 spaces
# print(f"{word:>20} {version}")
word = "Python"

print(f"{word:<20}")  # Left alignment
print(f"{word:>20}")  # Right alignment
print(f"{word:^20}")  # Center alignment

name = "AI"
print(f"{name:^10}")
