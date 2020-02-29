import random
hidden=random.randrange(1,100)
guess=input("Enter your number to guess")
result = bool(hidden==guess)
right= "You Guess it right!"
wrong= "Try again champ!"
out= lambda x: right if (result) else wrong
print(out(result))
