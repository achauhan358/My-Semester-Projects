#1/9/25

#Init
import random
score = 0
#functions
def mul_quiz():
    global score
    print("Welcome to the MULTIPLICATION QUIZ")
    question = input("How many questions do you want to answer?")
    level = input("Do you want easy(e) or hard(h) mode?")
    if level == "e":
        print("Sounds good! You'll get your score at the end. Let's begin!")
        for i in range (int(question)):
            num_1 = random.randint(0,5)
            num_2 = random.randint(0,5)
            user = input("What is " + str(num_1) + " times " + str(num_2))
            computer = num_1 * num_2
            if int(user) == computer:
                print("Correct!")
                score = score+1
            else:
                print("Incorrect :( The answer was "+ str(computer))
    if level == "h":
        print("Sounds good! You'll get your score at the end. Let's begin!")
        for i in range (int(question)):
            num_1 = random.randint(0,12)
            num_2 = random.randint(0,12)
            user = input("What is " + str(num_1) + " times " + str(num_2))
            computer = num_1 * num_2
            if int(user) == computer:
                print("Correct!")
                score = score+1
            else:
                print("Incorrect :( The answer was "+ str(computer))
    #score responses depend based off of % correct
    if score >= (int(question)*0.7):
        print("Nice job! You got " + str(score) + "/" + str(question))
    if score< (int(question)*0.7) and score>= (int(question)*0.4):
        print("You'll get it next time. You scored " + str(score) + "/" + str(question))
    if score < (int(question)*0.4) and score>=(int(question)*0):
        print("Remember, practice makes perfect. You scored " + str(score) + "/" + str(question))
#main
mul_quiz()
