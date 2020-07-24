import random
print("WELCOME TO KON BHANEGA CROREPATI")
name=input("Enter your name : ")
stage_one_questions=[["In which language was the book 'War and Peace' originally written?",["Russian","English","French","Spanish"]],
                     ["Which country is ruled by a single dynasty for more than two thousand years?",["Japan","England","Persia","Egypt"]],
                     ["Which is the capital of Afghanistan?",["Kabul","Baghdad","Teheran","Tashkent"]],
                     ["Who killed US President Abraham Lincoln?",["John Wilkes Booth","Lee Harvey Oswald","John Hinckley","Michael Schiavo"]],
                     ["Which of the following countries is landlocked?",["Switzerland","Italy","Spain","France"]],
                     ["Which is the national flower of Ireland?",["Shamrock","Daffodil","Marigold","Jasmine"]],
                     ["Where is Emperor Akbar’s tomb?",["Sikandra","Delhi","Agra","Amarkot"]]]

stage_two_questions=[["Who discovered the sea-route from Europe to India?",["Vasco-da-Gama","Christopher Columbus","Marco Polo","Magellan"]],
                     ["Who defined Democracy as the Government of the people, by the people and for the people?",["Abraham Lincoln","Winston Churchill","John Stuart mill","George Washington"]],
                     ["Which is the longest River in the world?",[" Nile","Amazon","Thames","Ganges"]],
                     ["Where is the headquarters of FIFA situated?",["Zurich","Sao Paulo","London","Dubai"]],
                     ["Which Asian mountain is also known as the Savage Mountain due to the extreme difficulty of ascent?",["K2","Kanchenjunga ","Lhotse","Mt.Everest"]]]

stage_three_questions=[["Apart from Venus, which planet rotates from east to west?",["Uranus","Jupiter","Mars","Saturn"]],
                       [" Which country was Herodotus referring to when he said: ‘There is no country that possesses so many wonders, nor any, that such a number of works that defy description’?",["Egypt","China","Germany","Greece"]],
                       ["Which is the largest internal organ in the human body?",["Liver","Brain","Heart","Lungs"]]]


random.shuffle(stage_one_questions)
random.shuffle(stage_two_questions)
random.shuffle(stage_three_questions)
stages=[stage_one_questions,stage_two_questions,stage_three_questions]
take_home_money=[0,41000,3591000]
game="Y"
count=1
prize= [1000,5000,10000,25000,50000,1000000,2500000,5000000,10000000]
won_money,correct=0,0
for a in range(0,3):
    if game=="Y" or game=="y":
        if count!=0:
            print("Welcome to Stage", a + 1)
            print()
            count=0
            for i in range(0,4-a):
                print("{},The question is for".format(name),prize[correct])
                print()
                print(stages[a][i][0])
                correct_answer=stages[a][i][1][0]
                random.shuffle(stages[a][i][1])
                for j in range(1,5):
                    print(j,stages[a][i][1][j-1])
                player_answer=int(input ("Enter the option number : "))
                print()
                if stages[a][i][1][player_answer-1]==correct_answer:
                    print("Correct")
                    print("You won",prize[correct])
                    won_money = won_money + prize[correct]
                    count+=1
                    correct+=1
                    print()

                else:
                    print("False")
                    print("The answer is",correct_answer)
                    print("GAME OVER")
                    count=0
                    print("You have won",take_home_money[a])
                    input()
                    break
            if won_money<10000000:
                if count!=0:
                    print("Your Total: ", won_money)
                    game = input("Do you wish to continue?Y/N")
                    print()

            else:
                print("{}, YOU HAVE WON KON BHANEGA CROREPATI".format(name))
                input()
        else:
            break

    else:
        print("You have won the money of",won_money)
        input()
        break

