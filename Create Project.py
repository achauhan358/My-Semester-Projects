#Annika Chauhan
#3/14/25

#init
import random
colors = ["RED", "ORANGE", "YELLOW", "BLACK",  "BROWN", "GREEN", "BLUE", "PURPLE", "WHITE", "PINK"]
vibes = ["PASSIONATE, BOLD, INTENSE, ENERGETIC, DYNAMIC", "VIBRANT, WARM, PLAYFUL, CREATIVE, EXUBERANT", "SUNNY, FRESH, HOPEFUL, OPTIMISTIC, CHEERFUL", "MYSTERIOUS, CHIC, POWERFUL, ELEGANT, SOPHISTICATED", "EARTHY, STABLE, RUSTIC, RELIABLE, WARM", "REFRESHING, BALANCED, GROWTH, CALMING, NATURAL", "CALM, RELIABLE, REFLECTIVE, SERENE, TRUSTWORTHY", "REGAL, CREATIVE, MYSTICAL, LUXURIOUS, INSPIRING", "PURE, MINIMALISTIC, PEACEFUL, CLEAN, FRESH", "PLAYFUL, ROMANTIC, SOFT, SWEET, TENDER"]
vibeslist = []
#func
def menu():
    while True:
        print("""1. Color vibes (regular colors)
2. Random color generator
3. Personality Test
4. Print all color options
5. Quit""")
        x = input("What would you like to do (enter number)?")
        if x == "1":
            cvibes(input("Enter desired vibe:").upper())
        elif x == "2":
            generator()
        elif x == "3":
            test()
        elif x == "4":
            print(colors)
        elif x == "5":
            break
        else:
            print("not an option, try again")

def test():
    print("Welcome to the color analyzer paint test!")
    x = int(input("Do you like sweet (1) or salty (2) treats?"))
    y = int(input("Do you like dogs (1) or cats (2)?"))
    z = int(input("Do you like coffee (1) or juice (2)"))
    total = x + y +z
    if total%2 == 1:
        print("You should paint your wall a warm color - let's continue with one last question")
        print("""What would you do in a zombie apocolypse?
a. run
b. hide
c. sacrifice someone
d. fight
e. die""")
        w = input("Which option do you choose?")
        if w == "a":
            print("You should paint your wall BROWN")
        if w == "b":
            print("You should paint your wall ORANGE")
        if w == "c":
            print("You should paint your wall YELLOW")
        if w == "d":
            print("You should paint your wall RED")
        if w == "e":
            print("You should paint your wall BLACK")
    if total%2 == 0:
        print("You should paint your wall a cold color - let's continue with one last question")
        print("""You find out your significant other cheated on you, what do you do?
a. attack them
b. cry
c. destroy their stuff
d. therapy
e. eat""")
        so = input("Which option do you choose")
        if so == "a":
            print("You should paint your wall PURPLE")
        if so == "b":
            print("You should paint your wall BLUE")
        if so == "c":
            print("You should paint your wall GREEN")
        if so == "d":
            print("You should paint your wall WHITE")
        if so == "e":
            print("You should paint your wall PINK")

def generator():
    color1 = random.randint(0,255)
    color2 = random.randint(0,255)
    color3 = random.randint(0,255)
    print(str(color1), str(color2), str(color3))
    print("Google the color (I recommend rgb.to) and see if it matches your mood")

def cvibes(vibe):
    f = 0
    vibeslist.clear()
    while True:
        for i in range(len(colors)):
            if str(vibe) in vibes[i]:
                vibeslist.append(colors[i])
                f = 1
        if f == 1:
            print(vibeslist)
        if f == 0:
            print("Trait not found")
        break
#main
cvibes(input("Welcome to paint vibe generator! I'm here to help get rid of your indecisiveness by focusing on color vibes. Please enter desired vibe:").upper())
