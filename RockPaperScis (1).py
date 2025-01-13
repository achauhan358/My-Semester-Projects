#1/7/24
#Rock Paper Scissors

#Init
import random
#Functions
wins=0 #sets the wins loss and ties at 0 for each time function runs from beginning
loss=0
ties = 0

def rps():
    print("Welcome player to ROCK PAPER SCISSORS")
    while True: #loop until user presses 4
        move = input("Please enter your move: rock(1), paper(2), scissors(3), quit game(4)")
        computer = random.randint(1,3)
        global wins
        global loss
        global ties
        #1 = rock
        #2 = paper
        #3 = Scissors
        #DRAWS
        if move == "1" and computer == 1:
            print("DRAW. You both picked ROCK")
            ties = ties + 1
            print ("score is now: " + str(wins) +" - " + str(loss) + " - ties: " + str(ties))
        if move == str(2) and computer == 2:
            print("DRAW. You both picked PAPER")
            ties = ties + 1
            print ("score is now: " + str(wins) +" - " + str(loss) + " - ties: " + str(ties))
        if move == str(3) and computer == 3:
            print("DRAW. You both picked SCISSORS")
            ties = ties + 1
            print ("score is now: " + str(wins) +" - " + str(loss) + " - ties: " + str(ties))
        #LOSS
        if move == str(1) and computer == 2:
            print("you lose:( the computer picked PAPER")
            loss = loss + 1
            print ("score is now: " + str(wins) +" - " + str(loss) + " - ties: " + str(ties))
        if move == str(2) and computer == 3:
            print("you lose:( Computer picked SCISSORS")
            loss = loss + 1
            print ("score is now: " + str(wins) +" - " + str(loss) + " - ties: " + str(ties))
        if move == str(3) and computer == 1:
            print("you lose:( Computer picked ROCK")
            loss = loss + 1
            print ("score is now: " + str(wins) +" - " + str(loss) + " - ties: " + str(ties))
        #WINS
        if move == str(2) and computer == 1:
            print("you win! Computer picked ROCK")
            wins = wins + 1
            print("score is now: " + str(wins) +" - " + str(loss) + " - ties: " + str(ties))
        if move == str(3) and computer == 2:
            print("you win! Computer picked PAPER")
            wins = wins + 1
            print ("score is now: " + str(wins) +" - " + str(loss) + " - ties: " + str(ties))
        if move == str(1) and computer == 3:
            print("you win! Computer picked SCISSORS")
            wins = wins + 1
            print ("score is now: " + str(wins) +" - " + str(loss) + " - ties: " + str(ties))
        if move == "4":
            break


#Main
rps()
