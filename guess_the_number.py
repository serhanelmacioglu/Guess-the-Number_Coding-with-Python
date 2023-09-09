import random
number = random.randint(1, 10)

player_name = input("Hello, what is your name? ")

number_of_guesses = 0

print('I\'m glad to meet you! {} \nLet\'s play a game with you, I will think a number between 1 and 10 then you will guess, alright? \nDon\'t forget! You have only 5 chances so guess:'.format(player_name))

while number_of_guesses < 5:
    guess = int(input())
    
    number_of_guesses += 1
    
    if guess > 10 or guess < 1: #checking if within range
        print(f'Number of out of range. The number must be between 1 and 10')
        print(f'You now have {5 - number_of_guesses} chances left')
    elif guess < number: #checking if less than the correct number
        print(f'Your estimate is too low, go up a little!')
        print(f'You now have {5 - number_of_guesses} chances left')
    elif guess > number: #checking if higher than the correct number
        print(f'Your estimate is too high, go down a bit!')
        print(f'You now have {5 - number_of_guesses} chances left')
    else: # The number is correct
        print(f'Congratulations {player_name}, you guessed the number in {number_of_guesses} tries!')
        break
    if number_of_guesses == 5:
        break
    else:
        continue

print(f'Close but no cigar, you couldn\'t guess the number. \nWell, the number was {number}')
