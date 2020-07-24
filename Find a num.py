import random as ra
c="Y"
count,counts,score,highest=0,0,0,0
while c=="Y" or "y":
    if score>highest:
        highest=score
    print("High Score: ",highest )
    print("Current Score: ",score )
    b = ra.randint(0, 101)
    d = True
    while d:
        if count < 9:
            a = int(input("Enter a number "))
            if a < b:
                print("The number is low")
                count+=1
            elif a > b:
                print("The number is high")
                count+=1
            else:
                print("You have entered the correct answer.You won!!")
                print("Number of tries:", count)
                score=100-(count*10)
                print("Score: ",score)
                c = input("Do you want to play again?Y/N")
                count=0
                d = False
        else:
            print("GAME OVER")
            c = input("Do you want to play again?Y/N")
            score=0
            count=0
            d = False


