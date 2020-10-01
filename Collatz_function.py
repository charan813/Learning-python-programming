def collatz(number):
   # defining the function for collatz sequence
    if number%2==0:
        result=number//2
        print(result)
        return(result)
    else:
        result=3*number+1
        print(result)
        return(result)
    
 #taking input for the collatz sequence   
number = int(input("Please Enter a number :"))

try:
    while (number)!=1: # loop to call the collatz function
        number= collatz(number)

except ValueError:
    print("you didnt enter a number")
