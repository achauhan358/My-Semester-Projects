#10/9/24

#Clickbait Headline Generator
#init

#functions
def believeHeadline1():
    noun = input("Please enter a noun:")
    ppronoun = input("Please enter a possesive pronoun:")
    place = input("Please enter a place:")
    print("You Won't Believe What This " +noun+ " Found in "+ ppronoun+ " "+place) #headline
def believeHeadline2():
    number = input("Please enter a number:")
    adjective = input("Please enter an adjective:")
    noun = input("Please enter a noun:")
    print(str(number)+ " "+adjective + " "+noun+ " Tricks You Didn't Know") #headline
def believeHeadline3():
    adjective = input("Please enter an adjective:")
    noun = input("Please enter a noun:")
    year = input("Please enter a year:")
    print("The "+ adjective+ " "+ noun +" Trends of " + year + " (you won’t believe #9)") #headline
#main
believeHeadline1()
believeHeadline2()
believeHeadline3()
