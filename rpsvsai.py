import random
player_wins= 0
computer_wins= 0
while player_wins<2 and computer_wins<2:
    
    print("Rock...")
    
    print("Paper...")
    
    print("Scissors...")
    
    p1= input("Player 1 make your move : ")
    
    rand_num=random.randint(0,2)
    if rand_num== 0:
        p2="rock"
    elif rand_num==1:
        p2="scissors"
    else:
        p2="paper"
    print(f"Player 2 plays {p2}")
        
    if p1==p2:
        print("Its a tie!")
    elif p1 == "rock":
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
        