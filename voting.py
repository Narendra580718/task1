user_name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")

elif age > 18:
    print(f"Dear {user_name}, your vote has been submitted.")

elif age < 18:
    print(f"Dear {user_name}, sorry, you need to be 18 or above to submite your vote.")

elif age == 18:
    print(f"Dear {user_name}, your vote has been submitted.")