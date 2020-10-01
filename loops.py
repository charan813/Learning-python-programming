import random
rand_num = random.randint(1, 10)
guess = None
while True:
    while guess != rand_num:
        guess = input("Pick a number from 1 to 10: ")
        guess = int(guess)
        if guess == rand_num:
            print("You got it!")
        elif guess < rand_num:
            print(" too LOW!")
        else:
            print("Too High!")

    play_again = input("Do you want to play again? (y/n)")
    play_again = str.lower(play_again)
    if play_again == "n":
        print("Thank you for playin!")
        break
    else:
        rand_num = random.randint(1, 10)
        guess = None


print(rand_num)
