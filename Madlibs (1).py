#12/9/24

#Init
#functions
def madlibs():
    print("""Welcome to Madlibs, a place for you to generate a fun story by filling in the blanks
          follow the suggested inputs to get your funny story""")
    place = input("Please enter a place:")
    digit = input("Please enter a number:")
    noun = input("Please enter a plural noun:")
    verb = input("Please enter a verb:")
    place1 = input("Please enter a place:")
    print("A duck went to " + place + " and bought " + str(digit) + " " + noun + ". Later the duck had to explain what" )
    print("the " + noun + " were needed for. He said the " + noun + " were needed to " + verb + " to " + place1)
#Main
madlibs()
