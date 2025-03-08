import random

print("DICE SIMULATOR")
while(True):
    x=random.randint(1,6)
    print(x)
    
    match x:
       case 1: 
             print("----------")
             print("|        |")
             print("|   0    |")
             print("|        |")
             print("----------")
       case 2:
            print("----------")
            print("|        |")
            print("|   0 0  |")
            print("|        |")
            print("----------")
       case 3:
            print("----------")
            print("|  0  0  |")
            print("|        |")
            print("|   0    |")
            print("----------")
            
       case 4:
            print("----------")
            print("|  0   0 |")
            print("|        |")
            print("|  0   0 |")
            print("----------")
       case 5:
            print("----------")
            print("| 0   0  |")
            print("|   0    |")
            print("| 0   0  |")
            print("----------")
       case 6:
            print("----------")
            print("| 0    0 |")
            print("| 0    0 |")
            print("| 0    0 |")
            print("----------")
            
       case default:
            print("wrong input")
    
    y=int(input("Want to roll again:\n1: to continue\n0: to break"))
    if y==0:
        break
    else:
        continue  