''' 
1 for snake
-1 for water
0 for gun
'''
import random
computer=random.choice([1,-1,0])
youstr=input("Enter your choice: ")                       #ENTER s for snake, w for water and g for gun
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake", -1:"water", 0:"gun"}
you=youDict[youstr] 
print(f"Computer chose {reverseDict[computer]}")
print(f"You chose {reverseDict[you]}")
if(computer == you):
    print("It's a tie!!!")
else:
    if((you==1 and computer==-1) or (you==-1 and computer==0) or (you==0 and computer==1)):
        print("You win!!!")
    else:
        print("You lose><")

