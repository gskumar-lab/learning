todo_list=[]
completed=False
while not completed:

    task=input("Enter the list of tasks to do: ")

    if len(task) == 0:
          
        completed=True

    else:
        todo_list.append(task)
        print("A task added")
         

print("\n TO-DO LIST\n"+"\n"+"*"*30)
for tasks in todo_list:

    print(tasks)


