# for i in range(1,20):
#     if i==4 or i==13:
#         print(f"{i} is UNLUCKY!!")
#     elif i%2!=0:
#         print(f"{i} is odd")
#     else:
#         print(f"{i} is even")

# for i in range(1,11):
#     print("\U0001f600"*i)       
# i=1    
# while i<11:
#     print("\U0001f600"*i)
#     i+=1


space=" "
times=10
for x in range(1,11):
    print(f"{space}"*times + "\U0001f600"* x)
    times-=1