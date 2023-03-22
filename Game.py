#!/usr/bin/env python
# coding: utf-8

# # Rock Paper Scissors

# In[5]:


#import 
from random import randint
score1 = 0 
score2 = 0
print('Welcome')

#player name
user=input('Please Enter Your Name :  ')
print('Lets start the game',user)
print('')

#no. of rounds
rounds=3
user_input = input('How many rounds do you want to play?')
try:
    rounds = int(user_input)
except ValueError:
    print('Not a number')
    
#loop for game
for i in range (rounds):
    player = input('Please choose between: \nrock(r), paper(p) or scissors(s)?').lower()

    if player =='r':
        print('\N{medium black circle}', end=' ')

    elif player == 'p':
        print('\N{page facing up}', end=' ')

    elif player == 's':
        print('\N{black scissors}', end=' ')

    else:
        print('??')

    print('vs', end=' ')
    
    #random pick by computer
    chosen = randint(1,3)

    if chosen == 1:
        computer ='r'
        print('\N{medium black circle}')

    elif chosen == 2:
        computer = 'p'
        print('\N{page facing up}')

    else:
        computer = 's'
        print('\N{black scissors}')

    if player == computer:
        print('DRAW!')
        print(' ')

    elif player == 'r' and computer == 's':
        print('Player wins! rock beats scissor')
        print(' ')
        score1 = score1+ 1

    elif player == 'r' and computer == 'p':
        print('Computer wins paper beats rock')
        print(' ')
        score2 = score2 + 1

    elif player == 'p' and computer =='r':
        print('Player wins! paper beats rock')
        print(' ')
        score1 = score1+ 1

    elif player == 'p' and computer == 's':
        print('Computer wins! scissor beats paper')
        print(' ')
        score2 = score2 + 1

    elif player == 's' and computer == 'p':
        print('Player wins! scissor beats paper')
        print(' ')
        score1 = score1 + 1

    elif player == 's' and computer =='r':
        print('Computer wins! rock beats scissor')
        print(' ')
        score2 = score2 + 1
        
    else:
        print('Huh?')
        print(' ')

#results according to scores        
if score1 < score2:                      
    print ("Your score is", score1)
    print ("Computers socre is",score2)
    print ("Computer wins!.")

if score1 > score2:
    print ("Your score is", score1)
    print ("Computers socre is",score2)
    print ("You win!.")

if score1 == score2:
    print ("Your score is", score1)
    print ("Computers socre is",score2)
    print ("Its a tie!!.")


# In[ ]:




