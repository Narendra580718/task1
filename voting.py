user_name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")

if age > 18:
    print("Vote submitted.")

if age < 18:
    print("Sorry, you need to be 18 or above to submite your vote.")

if age == 18:
    print("Vote submitted.")