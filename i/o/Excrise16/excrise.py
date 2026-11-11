#  Exercise 16. Interactive menu

print("1. Say Hello\n2. Calculate Square\n3. Exit")
choice = input("Enter choice (1-3): ")

if choice == "1":
    print("Hello there! Hope you're having a great day.")
elif choice == "2":
    val = int(input("Enter number to square: "))
    print(f"The square is: {val * val}")
elif choice == "3":
    print("Exiting... Goodbye!")
else:
    print("Invalid choice. Please pick 1, 2, or 3.")
 