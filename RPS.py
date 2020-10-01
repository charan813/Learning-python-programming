print("Rock... ")
print("Scissors... ")
print("Paper... ")

p1 = input("Player 1! Make your move( choose between rock,paper and scissors): ")
p2 = input("Player 2! Make your move( choose between rock,paper and scissors): ")

if p1 == "rock" and p2 == "scissors":
    print("Player 1 Wins!")
elif p1 == "rock" and p2 == 'paper':
    print("Player 2 Wins!")
elif p1 == "scissors"and p2 == "paper":
    print("player 1 Wins!")
elif p1 == "scissors" and p2 == "rock":
    print("Player 2 Wins!")
elif p1 == "paper" and p2 == "rock":
    print("Player 1 Wins!")
elif p1 == "paper" and p2 == "scissors":
    print("Player 2 Wins!")
elif p1 == p2:
    print("Its a tie")
else:
    print("input wasnt detected, Please restart")
