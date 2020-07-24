"""
WAP to introduce yor name and check if it knows you.
more options to forget your name
and also display the list
"""
name_list=[]
condition=True
while condition:
    option = input("""
            Select  options\n
                0.Exit\n
                1.Check if I know you\n
                2.Introduce Yourself\n
                3.Forget yor name\n
                4.List of person I knew\n
                Choose a number:\t
                 """)
    if option =="0":
        condition = False
    elif option== "1":
        name=input("Enter a name: ")
        if name in name_list:
            print("I know you")
        else:
            print("I don't know you")
    elif option == "2":
        name=input("Enter name: ")
        if name in name_list:
            print("I already know you")
        else:
            name_list.append(name)
    elif option == "3":
        name=input("Enter name to forget: ")
        if name in name_list:
            name_list.remove(name)
        else:
            print("name is not in the list")
    elif option == "4":
        print("Name list are ".join(name_list))
    else:
        condition=False
    input("")
print("last line")
