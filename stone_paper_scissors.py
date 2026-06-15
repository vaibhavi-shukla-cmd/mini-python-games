''' 1 for stone
-1 for paper 
0 for scissors

'''
import random
computer=random.choice([1,-1,0])
youstr=input("Enter your choice: ")                               #ENTER s for stone, p for paper and sc for scissors
youdict={"s":1,"p":-1,"sc":0}                                   
you=youdict[youstr]
reverseDict={1:"stone", -1:"paper", 0:"scissors"}
print(f"you chose {reverseDict[you]}")                      
print(f"computer chose {reverseDict[computer]}")
if(you==computer):
    print("It's a tie!!!")
else:
    if((you==1 and computer==0) or (you==-1 and computer==1) or (you==0 and computer==-1)):
        print("You win!!!")
    else:
        print("You lose><")