#print("g**3-x=0")
#x=int(input("what x to find the cube root of?: "))
#g=float(input("What guess to start with?: "))
#print("current estimate cubed= ", g**3)
#next_g=g-((g**3-x)/(3*g**2))
#print("Next guess to try=",next_g)
#num=3000
#fraction=1/3
#print(f"{num*fraction} is {fraction*100}% of {num}")
#print(2==3)
#print(2!=3)
#secret_number = str(71)
#user_n = str(input("guess the secret number: "))
#print(user_n == secret_number)
#print(3>2)

#pset_time = int(input("How many hours do you need to spend on the pset? "))
#sleep_time = int(input("How many hours do you need to sleep? "))
#if (pset_time + sleep_time) > 24:
    #print("impossible!")
#elif (pset_time + sleep_time) >= 24:
    #print("full schedule!")
#else:
    #leftover = abs(24-pset_time-sleep_time)
    #print(leftover,"h of free time!")
#print("end of day")

#x= int(input("Enter a number for x: "))
#y= int(input("Enter a different number for y: "))
#if x==y:
#    print(x,"is the same as",y)
#elif x>y:
#    print(x,"is greater than",y, "let's gooo")
#else:
#    print(y,"is greater than",x, "aww")
#print("end of program")    

sec_num= 11
guess= int(input("guess my secret number hehehe: "))
if guess==sec_num:
    print("n-no! that's not it... ok fine, you got it. baka. hmph.")
elif guess>sec_num:
    print("hold your horses buddy, it's not THAT high. try again.")
    new_guess= int(input("lets hear it: "))
    if new_guess==sec_num:
        print("you got it. barely. I mean a toddler could have done it if they tried that much. anyways congrats I guess.")
    elif new_guess>sec_num:
        print("yeah you like it high, don't you? just give up.")
    elif new_guess<sec_num:
        print(" you don't have a middle ground, do you? go again, from the TOP.")
elif guess<sec_num:
    print("OH! YOU GOT IT!.. lol. nah you suck. try again.")
    higher_guess= int(input("try to put a higher number this time: "))
    if higher_guess==sec_num:
        print("finally.")
    elif higher_guess>sec_num:
        print("k. that's too much. play again.")
    elif higher_guess<sec_num:
        print("I SAID HIGHER DANG IT! play again! gosh!")
print("This isn't the last you see of me! -tsundere secret number game")
            