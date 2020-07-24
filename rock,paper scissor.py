from random import randint
b=randint(1,4)
P1count,P2count=0,0
best=int(input("Enter the best of : "))
for i in range(0,best):
    a=int(input("""
        1.Rock
        2.Paper
        3.Scissor
        Enter the number    """))
    if a==1:
        if b!=2 :
            if b!=1:
                print("Player 1 used Rock.")
                print("Player 2 used Scissor")
                print("Player 1 won!")
                P1count+=1
            else:
                print("Player 1 used Rock.")
                print("Player 2 used Rock.")
                print("Its a draw")
        else:
            print("Player 1 used Rock.")
            print("Player 2 used Paper.")
            print("Player 2 won!")
            P2count+=1
    elif a==2:
        if b!=3:
            if b!=2:
                print("Player 1 used Paper.")
                print("Player 2 used Rock")
                print("Player 1 won!")
                P1count += 1
            else:
                print("Player 1 used Paper.")
                print("Player 2 used Paper.")
                print("Its a draw")
        else:
            print("Player 1 used Paper.")
            print("Player 2 used Scissor.")
            print("Player 2 won!")
            P2count += 1
    else:
        if b!=1:
            if b!=3:
                print("Player 1 used Scissor.")
                print("Player 2 used Paper")
                print("Player 1 won!")
                P1count += 1
            else:
                print("Player 1 used Scissors.")
                print("Player 2 used Scissor.")
                print("Its a draw")
        else:
            print("Player 1 used Scissor.")
            print("Player 2 used Rock.")
            print("Player 2 won!")
            P2count += 1
print(P1count,"-",P2count)
if P1count>P2count:
    print("You won!!")
elif P2count>P1count:
    print("You lost!!!!!!!")
else:
    print("ITs a DRAW..")
input()
