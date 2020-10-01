import random
rand_num = random.randint(0, 2)
print("Rock... ")
print("Scissors... ")
print("Paper... ")

p1 = input("Player 1! Make your move( choose between rock,paper and scissors): ").lower()
if rand_num == 0:
    c1 = "rock"
elif rand_num == 1:
    c1 = "paper"
elif rand_num == 2:
    c1 = "scissors"

print(f"Computer plays {c1}")

if p1 == "rock" and c1 == "scissors":
    print("Player 1 Wins!")
elif p1 == "rock" and c1 == 'paper':
    print("computer Wins!")
elif p1 == "scissors"and c1 == "paper":
    print("player 1 Wins!")
elif p1 == "scissors" and c1 == "rock":
    print("computer Wins!")
elif p1 == "paper" and c1 == "rock":
    print("Player 1 Wins!")
elif p1 == "paper" and c1 == "scissors":
    print("Computer Wins!")
elif p1 == c1:
    print("Its a tie")
else:
    print("input wasnt detected, Please restart")
