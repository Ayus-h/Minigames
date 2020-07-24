row=["AFKPUZ","BGLQV","CHMRW","DINSX","EJOTY"]
horizontal=["ABCDE","FGHIJ","KLMNO","PQRST","UVWXY","Z"]
word=True
length=1
entire_word=""
while word:
    print("1 2 3 4 5 6")
    for i in row:
        string = ""
        for j in i:
            string+=j+" "
        print(string)
    first_input=int(input("Enter the the column number your letter is in : "))
    print("1 2 3 4 5 6")
    for i in horizontal:
        string = ""
        for j in i:
            string+=j+" "
        print(string)
    second_input=int(input("Enter the the column number your letter is in : "))

    for i in horizontal[first_input-1]:
        for j in row[second_input-1]:
            if i==j:
                entire_word+=i
                print(length,"letter/s found")
                next_word=input("Do you want to continue for next letter in your word?(y/n)")
                length+=1
                if next_word!="y":
                    word=False
print(entire_word)
print("You guessed this letter, didn't you?")
input()





