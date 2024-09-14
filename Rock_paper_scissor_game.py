import random as rn

#ROCK , PAPER AND SCISSOR
def Rock_game(comp,you):
    if(comp==you):
        print("GAME TIE!")
        return
    elif(comp=="r"):
       if(you=="p"):
           return True
       if(you=="s"):
           return False
       
    elif(comp=="p"):
        if(you=="s"):
            return True
        if(you=="r"):
            return False
        
    elif(comp=="s"):
        if(you=="r"):
            return True
        if(you=="p"):
            return False    
        
print("COMPUTER TURN :ROCK(r), PAPER(p) AND SCISSOR(s)?")
random_num=rn.randint(1,3)
if random_num==1:
        comp='r'
elif random_num==2:
        comp='p'
elif random_num==3:
        comp='s'
      
print()
you=input("YOUR TURN :ROCK(r),PAPER(p) AND SCISSOR(s)?")

#VALIDATE INPUT
if you not in ['r','p','s']:
  print("INVALID INPUT! PLEASE CHOOSE 'r', 'p' and 's'")
else:
  a=Rock_game(comp,you)
  print(f"COMPUTER CHOOSE:{comp}")
  print(f"YOU CHOOSE:{you}")
    
  if(a is None):
   print("THE GAME IS TIE !")
  elif a:
    print("YOU WIN .....")
  else:
    print("YOU LOSE .....")