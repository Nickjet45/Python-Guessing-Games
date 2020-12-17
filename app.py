import random

#Function to have the user guess a number between 0 and 100
def guess_Number():
    #Initializes the variable at -1, since -1 will never be the actual number 
    guessed_number = -1

    #Stores a random value between 0 and 100 into the variable hidden_number
    hidden_number = random.randint(0, 100)

    #Keeps track of the number of guesses the user has tried
    current_guesses = 0
    print("I'm thinking of a number between 0 and 100 please guess it...")

    #While the user has not guessed the correct number
    while guessed_number is not hidden_number:
        #Increase the number of guesses by 1
        current_guesses += 1

        #Prompt the user for their guess
        guessed_number = int(input('Please guess the number '))

        #If the user guesses above the number, tell them to guess lower
        if guessed_number > hidden_number:
            print('The number is lower please guess again')
        
        #Else if the user guesses below the number, tell them to guess higher
        elif guessed_number < hidden_number:
            print('The number is higher please guess again')
        
        #Else if the user guesses the number, tell them they have guessed it along with how many tries it took them
        elif guessed_number == hidden_number:
            print('You have correctly guessed the number which was {}'.format(hidden_number))
            print('It took you {} guesses'.format(current_guesses))
            break

#Function to roll an X sided dice, where X is the number of sides determined by the user
def roll_Dice():
    #Ask the user if they would like to roll the dice
    response = input('Would you like to roll the dice?[Y/N] ')
    #If the user says yes roll the dice
    if 'y' in response:
        #While the user has not said no
        while True:
            #Ask them how many sides they would like for the dice to be
            number_of_sides = int(input('How many sides would you like for the dice to have? '))
            
            #Roll a random number between 1 and the number of sides
            rolled_number = random.randint(1, number_of_sides)

            #Output what side the program landed on
            print('You rolled {}'.format(rolled_number))

            #Prompt the user to roll the dice again
            new_response = input('Would you like to roll again?[Y/N] ')
            
            #if they say yes, restart the loop
            #Else exit the loop, and end the program
            if 'y' in new_response:
                print('Restarting program...')
            elif 'n' in new_response:
                print('Cancelling program...')
                break
    
    #if the user says no, cancel the program
    elif 'n' in response:
        print('Cancelling program....')
    
    #If the user says something which does not include the letter y or n, restart the program
    else:
        print('Invalid response, restarting program...')
        roll_Dice()


guess_Number()