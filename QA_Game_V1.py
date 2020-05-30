import time
print("""Welcome to the QA game. 
Please enter your first name:""")
name = input().capitalize()
print("""Thank you for coordination {0}.
Read all below instructions carefully.

1. You will be asked 10 questions each of 1 point.
2. Each question will have 4 options. Select the correct one.
3. Once you correctly answer question 5, negative marking will be started.
4. For example if you give wrong answer to question 6 then one point will be deducted and you will remain with 4 points 
instead of 5 points.
5. If you answer 6 question correctly then 1 point will be added, means you will have 6 points.
6. Good luck.
 """.format(name))

print("Shall we start {0} (1 for Yes or 2 for No)".format(name))
Dec = int(input())

option = [1, 2]
while Dec not in option:
    Dec = int(input("Invalid Input {}. Please select 1 for Yes and 2 for No.".format(name)))
if Dec == 1:
    print("Please wait ...")
    time.sleep(2)
elif Dec == 2:
    print("We will miss you.")
    exit()

print()
points = 0
lost = 0

print("""Q1. What is the name of Indian capital?
A. Kolkata
B. Delhi
C. Chennai
D. Mumbai""")

print("Write your answer: ")
Ans1 = input().capitalize()
if Ans1 == "B":
    print("You are Correct {0}.".format(name))
    points = points+1
    print("Your points {0}".format(points))
else:
    lost =lost + 1
    print("You are wrong.")
    print("Your points {0}".format(points))
time.sleep(1)
print()


print("""Q2. Which one of the below rivers does not belong to India?
A. Ganga
B. Amazon
C. Yamuna
D. Kaveri""")
print("Write your answer: ")
Ans2 = input().capitalize()
if Ans2 == "B":
    print("You are Correct {0}.".format(name))
    points = points + 1
    print("Your points {0}".format(points))
    if lost > 0:
        lost = lost - lost
else:
    lost = lost + 1
    print("You are wrong.")
    print("Your points {0}".format(points))

time.sleep(1)
print()


print("""Q3. Who is the current Prime Minister of India?
A. Rahul Gandhi
B. Amit Shah
C. Sonia Gandhi
D. Narendra Damodar Modi""")
print("Write your answer: ")
Ans3 = input().capitalize()
if Ans3 == "D":
    print("You are Correct {0}.".format(name))
    points = points + 1
    print("Your points {0}".format(points))
    if lost > 0:
        lost = lost - lost
else:
    lost = lost + 1
    print("You are wrong.")
    print("Your points {0}".format(points))
    if lost >= 3:
        print("Continuous 3 wrong answers. You are out")
        print("Thank you for playing with us {0}. Your points are {1}".format(name, points))
        exit()

time.sleep(1)
print()


print("""Q4. Who is the BCCI persident currently.
A. Sachin Tendulkar
B. Saurav Gangully
C. Rahul Dravid
D. Anil Kumble""")
print("Write your answer: ")
Ans4 = input().capitalize()
if Ans4 == "B":
    print("You are Correct {0}.".format(name))
    points = points + 1
    print("Your points {0}".format(points))
    if lost > 0:
        lost = lost - lost
else:
    lost = lost + 1
    print("You are wrong.")
    print("Your points {0}".format(points))
    if lost >= 3:
        print("Continuous 3 wrong answers. You are out")
        print("Thank you for playing with us {0}. Your points are {1}".format(name, points))
        exit()

time.sleep(1)
print()


print("""Q5. Which country had the strongest GDP 2019?
A. America
B. Britain
C. China
D. Australia""")
print("Write your answer: ")
Ans5 = input().capitalize()
if Ans5 == "A":
    print("You are Correct {0}.".format(name))
    points = points + 1
    print("Your points {0}".format(points))
    if lost > 0:
        lost = lost - lost
else:
    lost = lost + 1
    print("You are wrong.")
    print("Your points {0}".format(points))
    if lost >= 3:
        print("Continuous 3 wrong answers. You are out")
        print("Thank you for playing with us {0}. Your points are {1}".format(name, points))
        exit()

time.sleep(1)
print()
print("{}, Negative marking starts here. Each wrong answer will minus 1 point.".format(name))
time.sleep(1)
print()


print("""Q6. Who was the maternal uncle of Lord Krishna?
A. Shakuni
B. Ravan
C. Kansh
D. Bhishma""")
print("Write your answer: ")
Ans6 = input().capitalize()
if Ans6 == "C":
    print("You are Correct {0}.".format(name))
    points = points + 1
    print("Your points {0}".format(points))
    if lost > 0:
        lost = lost - lost
else:
    lost = lost + 1
    points = points - 1
    print("You are wrong.")
    print("Your points {0}".format(points))
    if lost >= 3:
        print("Continuous 3 wrong answers. You are out")
        print("Thank you for playing with us {0}. Your points are {1}".format(name, points))
        exit()

time.sleep(1)
print()


print("""Q7. When India celebrates Independence day?
A. 26 January
B. 1 May
C. 15 August
D. 5 September""")
print("Write your answer: ")
Ans7 = input().capitalize()
if Ans7 == "C":
    print("You are Correct {0}.".format(name))
    points = points + 1
    print("Your points {0}".format(points))
    if lost > 0:
        lost = lost - lost
else:
    lost = lost + 1
    points = points - 1
    print("You are wrong.")
    print("Your points {0}".format(points))
    if lost >= 3:
        print("Continuous 3 wrong answers. You are out")
        print("Thank you for playing with us {0}. Your points are {1}".format(name, points))
        exit()

time.sleep(1)
print()


print("""Q8. What is the name of Capital of West Bengal, India
A. Howrah
B. Burdwan
C. Durgapur
D. Kolkata""")
print("Write your answer: ")
Ans8 = input().capitalize()
if Ans8 == "D":
    print("You are Correct {0}.".format(name))
    points = points + 1
    print("Your points {0}".format(points))
    if lost > 0:
        lost = lost - lost
else:
    lost = lost + 1
    points = points - 1
    print("You are wrong.")
    print("Your points {0}".format(points))
    if lost >= 3:
        print("Continuous 3 wrong answers. You are out")
        print("Thank you for playing with us {0}. Your points are {1}".format(name, points))
        exit()

time.sleep(1)
print()


print("""Q9. Select the Longest river in India.
A. Ganga
B. Yamuna
C. Saraswati
D. Godawari""")
print("Write your answer: ")
Ans9 = input().capitalize()
if Ans9 == "A":
    print("You are Correct {0}.".format(name))
    points = points + 1
    print("Your points {0}".format(points))
    if lost > 0:
        lost = lost - lost
else:
    lost = lost + 1
    points = points - 1
    print("You are wrong.")
    print("Your points {0}".format(points))
    if lost >= 3:
        print("Continuous 3 wrong answers. You are out")
        print("Thank you for playing with us {0}. Your points are {1}".format(name, points))
        exit()

time.sleep(1)
print()


print("""Q10. Who is the founder of Facebook?
A. Bill Gates.
B. Jamshed Tata
C. Sunder Pichai
D. Mark Zukerburg""")
print("Write your answer: ")
Ans10 = input().capitalize()
if Ans10 == "D":
    print("You are Correct {0}.".format(name))
    points = points + 1
    print("Your points {0}".format(points))
    if lost > 0:
        lost = lost - lost
else:
    lost = lost + 1
    points = points - 1
    print("You are wrong.")
    print("Your points {0}".format(points))
    if lost >= 3:
        print("Continuous 3 wrong answers. You are out")
        print("Thank you for playing with us {0}. Your points are {1}".format(name, points))
        exit()

time.sleep(1)
print()

print("Thank you for playing with us {0}. Your points are {1}".format(name, points))
