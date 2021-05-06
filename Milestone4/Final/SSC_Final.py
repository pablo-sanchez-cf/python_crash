# Pablo Sanchez
# Python version 2.7.16
# Final Practical

# 4. Import Random Module - Put the answer on the next line.
import random

# 5. Create a variable named numbers. It needs to generate a number between 1 to 10.
# Put the answer on the next line. 
numbers = random.randint(1, 10)

# 6. Create a variable named player_name.  It needs to prompt the user to enter his/her name.
# Put the answer on the next line. 
player_name = str(raw_input('Enter your name: '))

# 7. Create a variable named number_of_guesses and assign 0 to it.
# Put the answer on the next line. 
number_of_guesses = 0

# 8. Print a string which includes the player_name variable. It should say: player_name, I am guessing a number between 1 and 10!
# Put the answer on the next line. 
print(player_name + ', I am guessing a number between 1 and 10!')

# 9. Create a WHIlE Loop. Give the user 5 attempts to guess the number. If the number is too low print Your guess is too low. If the number is too high print Your guess is too high. Create a break if the user answers it correctly.
while number_of_guesses < 5:



# 10. if/else Statements - Verifying if the user has guessed the number or not.. If they did...then print a message for them along with the number of tries. If the player couldnt guess the number at the end...print the number along with a message.


    guess = int(raw_input('Please pick a number from 1 to 10\n>> '))
    if guess < numbers:
        print('Your guess is too low')
        number_of_guesses +=1
    elif guess > numbers:
        print('Your guess is too high')
        number_of_guesses +=1
    elif guess == numbers:
        print('You guessed the correct number!')
        number_of_guesses +=1
        print(str(number_of_guesses) + ' tries')
        break
if number_of_guesses == 5:
    print("You've ran out of guesses.")
    print(str(number_of_guesses) + ' tries')