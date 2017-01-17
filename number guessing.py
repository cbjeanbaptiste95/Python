import random

def main():
    random_number = random.randint(1,100)

    guess = input("guess a number:")
    
    while guess != random_number:
        if guess > random_number:
            print("too high!")
        if guess < random_number:
            print ("too low!")
        guess = input("guess again!")
    if guess == random_number:
            print("you guessed it!")
if __name__ == "__main__":
    main()
