space = " "
for i in range(5):
    times = 10
    for x in range(1,11):
        print(f"{space}"*times +"\U0001f600" * x)
        times -= 1
    # t = 0
    # for x in range(21,0,-2):
    #     print(f"{space}"*times +"\U0001f600" * x)
    #     times += 2