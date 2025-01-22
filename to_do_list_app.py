
# A Basic To-do List App 
# a to-do list app where you can add, remove and mark tasks as complete 
import time
def to_do_list():
    print('\nTo-do list App')
    print('\nChoose an option')
    print('1. Add a Task')
    print('2. Remove a Task')
    print('3. Mark a task as Complete')
    print('4. View Tasks')
    print('5. Exit')


# add a task
def add_task():
    global tasks_list
    tasks_list = []

    while True:
        tasks = input("Enter a task(type 'q' to end adding a task): ").strip().title()
        if tasks.startswith('q') or tasks.startswith('Q'):
            break
        else:
            tasks_list.append(tasks)
            for task in tasks_list:
                print(f"'{task}' Added ") 
# remove_task
def remove_task():
    try:
        global tasks_list
        remove_task = input('What task do you want to remove: ').title().strip()
        if remove_task in tasks_list:
            list_comp = [task for task in tasks_list if remove_task in tasks_list]
            if list_comp:
                tasks_list.remove(remove_task)
                print(f'{remove_task} has been removed!')
        else:
            print('Invalid Input!')
    except NameError:
        print(f"Task '{remove_task}' not found")
    
    

# complete task
def complete():
    try:
        global tasks_list
        while True:
            task_done = input('What task have you completed(type none if you have not complete any)? ').title().strip()
            if task_done.startswith('none') or task_done.startswith('None'):
                break
            elif task_done in tasks_list:
                #for task in tasks_list:
                print(f"Task:\n- '{task_done}' : ✔ Complete!")
                break
            else:
                print(f"'{task_done}' not found")
    except NameError:
        print(f"Task'{task_done}' not found")
        
    
# view task
def view_task():
    try:
        global tasks_list
        if tasks_list == []:
            print('No task Available')
        for task in tasks_list:
            print(task)
    
    except:
        print("No Task Available")

# exit app 
def exit_app():
    print('Exiting the app. Goodbye!')
    time.sleep(1)
    exit()
    

        

def app():
        to_do_list()
        while True:
            choose = input('Choose an option(1-5): ').strip()
            if choose == '1':
                add_task()
            elif choose == '2': 
                remove_task()
            elif choose == '3': 
                complete() 
            elif choose == '4': 
                view_task() 
            elif choose == '5':
                exit_app()
            else: 
                print('Invalid Input!, Please try again')



            
    


if __name__ == '__main__':
    app()
