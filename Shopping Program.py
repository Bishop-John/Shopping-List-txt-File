print ("Welcome to the Shopping List Program")
print ("------------------------------------")
print ("Here you can... \n")
while True:
    print ("(V)iew list, \n(A)dd to list,, \n(C)lear the list, \n(O)rder list, \n(S)earch list.")


    action = input("What would you like to do...").upper()

    if action == "V":
        file = open("Shopping List.txt", "r")
        data = file.read()
        print (data)

    elif action == "A":
        newItem = input("What do you want to add...")
        file = open("Shopping List.txt", "a")
        file.write(newItem + "\n")
        file.close()
        print ("Item added")

    elif action == "C":
        file = open("Shopping List.txt", "w")
        file.write("")
        file.close()
        print ("List cleared")
        
    elif action == "O":
        file = open("Shopping List.txt", "r")
        lines = file.read().split("\n")
        lines.sort()
        del lines[0]
        print (lines)

    elif action == "S":
        searchItem = input("What are you looking for...")
        file = open("Shopping List.txt", "r")
        lines = file.read().split("\n")
        if searchItem in lines:
            print ("Yes this is in the list.")
        else:
            print ("No it is not in the list.")