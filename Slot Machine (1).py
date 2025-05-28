#Annika Chauhan
#1/29/25

#init
import random
import time
credit = 5
symbols= ['♥', '♦', '♠', '♣', '☆','7']
weights = [1,1,1,1,1,0.5]
#func
def machine():
    print("Welcome to the Slot Machine Casino! You have 5 credits")
    print("Three 7s is a JACKPOT (times 3 bet), Three of same symbol is a WIN (times 2 bet), and mismatched is a loss")
    spin = input("Would you like to spin or quit (s/q)").upper()
    global credit
    while True:
        if spin == "S":
            while True:
                bet = input("You have "+ str(credit) + " credits. How much do you want to bet?")
                try:
                    bet = int(bet)
                    if bet > credit:
                        print("You don't have enough credits. Enter another number.")
                    elif bet <= 0:
                        print("What?! Enter another number.")
                    elif bet <= credit:
                        print("Okay, let's spin!")
                        break
                except:
                    print("Oops! That isn't't a whole number")
            credit = credit - abs(int(bet)) #subtracts absolute value of bet in case user attempts to bet a negative amount
            print("spinning...")
            time.sleep(1)
            print("spinning...")
            time.sleep(1)
            print("spinning...")
            time.sleep(1)
            slot1 = random.choices(symbols, weights=weights, k=1) #random choice of list with different weights
            slot2 = random.choices(symbols, weights=weights, k=1) #random choice of list with different weights
            slot3 = random.choices(symbols, weights=weights, k=1) #random choice of list with different weights
            if slot1[0] == "7" and slot2[0] == "7" and slot3[0] == "7":
                credit = credit + (int(bet)*3) #adds credit accordingly
                print(str(slot1)+str(slot2)+str(slot3))
                print("Jackpot!! You have " + str(credit) + " credits")
                again = input("Would you like to play again (y/n)")
                if again == "n" and credit <= 0:
                    print("You ran out of money anyways. Come back soon to win big!")
                    break
                if again == "n" and credit > 0:
                    print("You won " + str(credit) + " credits! Come back soon!")
                    break
            elif slot1[0]==slot2[0]==slot3[0]:
                print(str(slot1)+str(slot2)+str(slot3))
                credit = credit + (2*int(bet)) #adds credit accordingly
                print("You won! You have " + str(credit) + " credits")
                again = input("Would you like to play again (y/n)")
                if again == "n" and credit <= 0:
                    print("You ran out of money anyways. Come back soon to win big!")
                    break
                if again == "n" and credit > 0:
                    print("You won " + str(credit) + " credits! Come back soon!")
                    break
            else:
                print(str(slot1)+str(slot2)+str(slot3))
                print("You lost :( You have " + str(credit) + " credits")
                again = input("Would you like to play again (y/n)")
                if again == "n" and credit <= 0:
                    print("You ran out of money anyways. Come back soon to win big!")
                    break
                if again == "n" and credit > 0:
                    print("You won " + str(credit) + " credits! Come back soon!")
                    break
        if credit <= 0 and again != "n":
                print("Too bad :( You lost all your money and have to leave")
                break
        if spin == "q":
            break


#main
machine()
