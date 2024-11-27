interests={'gsk':'fun','ravi':'money','suresh':'power'}



def add():
    completed=False

    while completed == False:
        person=input("enter the person to add : ")    
        if len(person)!=0:
            likes=input("enter the activity for "+person+" : ")
            interests[person]=likes
            completed=False
        else:
            completed=True
    menu()

def delete():
    completed=False

    while completed == False:
        person=input("enter the person to delete : ")    
        if len(person)!=0:
            del interests[person]
            completed=False
        else:
            completed=True
    menu()

def display():
    print("The Dictionary :\n"+"_"*30)
    for keys in interests:
        print(keys+" : "+interests[keys])
    print("*"*15)
    menu()

def menu():   
    userinput=input("The dictionary\n1.Add person\n2.Remove person\n3.Display current dictionary\n"+"-"*30+"\nPress enter to exit\n")
    
    completed=False
    while completed==False:

        if userinput=='1':
            add()
        elif userinput=='2':
            delete()
        elif userinput=='3':
            display()
        else:
            print("else")

        completed=True
        

    

menu()