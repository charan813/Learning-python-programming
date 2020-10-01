#ask for age
age = input("How old are you ? ")
if age:
#18-21 wristband
    if int(age) >=18 and int(age) <21:
        print(" You can enter but you Need a wristband")
#21+ drink normal entry
    elif int(age) >= 21 :
        print("you can enter and you are allowed to drink")
#too young, sorry
    else :
        print("you cant enter lil one")
else :
    print("please enter your age!")
