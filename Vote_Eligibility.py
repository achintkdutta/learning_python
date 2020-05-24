# This program will evaluate if the user is eligible to vote or not.

print("""Hi
Please enter your name: """)
name = input()
print("Please enter your age {0}:".format(name))
age = int(input())

if age >= 18:
    print("{0}, you are eligible for voting".format(name))
    print("Thank you")

else:
    calculate = 18-age
    print("{0}, you are not eligible for voting currently".format(name))
    print("You have to wait for {0} more years to be eligible for voting".format(calculate))
    print("Thank you")