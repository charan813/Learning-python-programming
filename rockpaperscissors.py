print("Rock...")

print("Paper...")

print("Scissors...")

p1= input("Player 1 make your move : ")
p2=input("Player 2 make your move : ")

if p1==p2:
    print("Its a tie!")
elif p1=="rock":
    if p2=="scissors":
        print("player 1 wins!")
    elif p2 =="paper":
        print("player 2 wins!")
elif p1=="scissors":
    if p2=="rock":
        print("Player 2 wins!")
    elif p2=="paper":
        print("player 1 wins!")
elif p1=="paper":
    if p2=="rock":
        print("Player 1 wins!")
    elif p2=="scissors":
        print("Player 2 wins!")
else:
    print("something went wrong")        
    