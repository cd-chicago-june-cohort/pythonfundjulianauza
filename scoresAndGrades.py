import random

x=1
while x <= 10:
    score = random.randint(0,100)
    print "score is:", score,

    grade=""

    if score > 90:
        grade = "A"
    elif score > 80:
        grade = "B"
    elif score > 70:
        grade = "C"
    elif score > 60:
        grade = "D"
    else:
        grade = "Flawless"

    print ":Your grade is",grade
    x+=1

