import random
print('Enter your name')
userName = input()
print('Hello ' + userName + ', Im guessing a number between 1 and 100')
randomNum = random.randint(1,100)

for guessestaken in range (1,6):
    print('Take a guess!')
    userNum = int(input())
    if userNum > randomNum:
        print('Thats too high')
        print('you have ' + str(5 - int(guessestaken))+ ' chance(s) left')
    elif userNum < randomNum:
        print('Thats too low')
        print('you have ' + str(5 - int(guessestaken))+ ' chance(s) left')
    else:
        break

if userNum == randomNum:
    print('Good job' + userName+ ', you have guessed it')
else:
    print('Sorry ' + userName + ', you are out of chances. I chose ' + str(randomNum))

