import random
number = random.randint(1, 10)

player_name = input("Hello, what is your name? ")
number_of_guesses = 0
print('I\'m glad to meet you! ' + player_name+ ' \nLet\'s play a game with you, I will think a number between 1 and 10 then you will guess, alright? \nDon\'t forget! You have only 3 chances so guess:')

while number_of_guesses < 3:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your estimate is too low, go up a little!')
    if guess > number:
        print('Your estimate is too high, go down a bit!')
    if guess == number:
        break
if guess == number:
    print( 'Congratulations '+ player_name + ', ' + 'you guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('Close but no cigar, you couldn\'t guess the number. \nWell, the number was ' + str(number) + '.')
