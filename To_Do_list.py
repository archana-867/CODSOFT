Tasks=[]

def create_task(task):
    Tasks.append((task,False))
    print(f'Task"{task}" added to the list.')

def update_task(index,new_task):
    if index<=0 or index>len(Tasks):
        print("invalid task number")
        return
    completed=Tasks[index-1]
    Tasks[index-1]=(new_task,completed)
    print(f'Task{index} updated to "{new_task}"')

def complete_task(index):
    if index <= 0 or index > len(Tasks):
        print("invalid tak number")
        return
    
    task,_=Tasks[index-1]
    Tasks[index-1]=(task,True)
    print(f'Task"{task}" marked as completed.')

def display_task():
    if not Tasks:
        print("No task in your to do list.")
    else:
        for index,(task,completed) in enumerate(Tasks,1):
            status="Done" if completed else "Not Done"
            print(f'"{index}.{task} - {status}"')

#creating  task
create_task("Wake up")
create_task("Do some domestic chors")
create_task("Get ready fast to go office")

#displaying task
print("\n current To Do list")
display_task()

update_task(2,"clean the entire room")

complete_task(1)

print("\n Updated TO DO list")
display_task()
