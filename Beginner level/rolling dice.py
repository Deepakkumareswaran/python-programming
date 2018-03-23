import random
flag = 1
min = 1
max = 6
input("press enter to  roll ")
while flag==1:
    e=random.randint(min,max)
    print(e)
    if(e==6 or e==1):
        print("you have another turn")
        input("press enter to roll the diec again..!")
        f=random.randint(min,max)
    else:
        print("your turn over")
        print ("Try Again...!")
        flag = 0
