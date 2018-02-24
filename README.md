# randonumero
I'm a noob so I created a random number simulator!

#import random and time modules
import random
import time

#print statement user will first see 
print("what's good my friends, want to play a game?")

#use a while loop to prompt user to insert an answer
while True:
    #create variable called 'button'
    #use 'input' function to allower user to type in an answer to our text question
    button = input("press 'y' if you want, but if you're boujee press 'n'")
    #use if statement to parse possible answer of 'y' or 'n'; everything else is not accepted
    #use button[0].lower() to convert the first letter of the user's answer to lower.
    # If the user's answer equals 'y' then we have a winner
    if button[0].lower() == 'y':
        print("Nice, let's get rolling then...")
        #use 'time' function
        # .sleep(n); n denotes how many seconds to wait until script pumps out answer
        time.sleep(2)
        #define variable 'num' to store random function in
        #use 'random' and 'randint' function
        #(1,11) denotes from 1-10 and excludes 11 in terms of possible random numbers to pick from
        num = random.randint(1,11)
        print(num)
    elif button[0].lower() == 'n':
        print("Damn, you boujee! You gotta leave now...")
        time.sleep(2)
        #break statement stops loop
        break
    else:
        print("Nah bruh you gotta type either 'y' or 'n'")
        #continue statement brings the user to the beginning of the loop
        continue
