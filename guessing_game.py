import random
Number=random.randint(1,100)
while True:
    a=int(input('Guess the Number between 1 and 100:'))
    if a==Number:
        print('Your Guess was on Spot!!')
        break
    elif a>Number:
        print('Your Guess was too High!!')
    elif a<Number:
        print('Your Guess was too Low!!')
