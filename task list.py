def create(list_task):
    for task in list_task:
        if task != new_task:
            task_list['task'].append(new_task)
            return
        else:
            continue
    return


def delete_task(list_task):
    for task in list_task:
        if task == del_task:
            task_list['task'].pop(list_task.index(task))
            return
        else:
            continue
    return


def completed(list_task):
    for task in list_task:
        if task == done:
            task_list['completed'].append(task + '\u0336')
            list_task.pop(list_task.index(task))
            return
        else:
            continue
    return


def edit(list_task):
    for task in list_task:
        if task == edit_task:
            task_list['task'].pop(task_list['task'].index(task))
            task_list['task'].append(input('Change your task'))
            return
        else:
            continue


print('Hi! This your task list.Сhoose what you want to do')
task_list = {'task': [''], 'completed': ['']}
while True:
    choose = input('1. Create new task.\n2. Delete task.\n3. Edit task.\n4. See the list of task\n5. Exit\n')
    if choose == '1':
        print('You have chosen to create a new task')
        new_task = input('Enter your new task')
        create(task_list['task'])
        print('You have 1 task', task_list['task'])
        continue
    elif choose == '2':
        print('You have chosen to delete a task')
        del_task = input('Enter what task do you want to delete')
        delete_task(task_list['task'])
        print('This task deleted')

    elif choose == '3':
        print('You have chosen to edit a task')
        edit_done = input('you want to change the task or mark it as completed\n1.Edit\n2.To perform the task')
        if edit_done == '1':
            edit_task = input('Enter which task you want to change')
            edit(task_list['task'])
        else:
            done = input('what task did you complete')
            completed(task_list['task'])
    elif choose == '4':
        print('you have chosen to see the list of task')
        actual_done = input('what task list do you want to see\n1.Actual tasks\n2.Completed tasks\n3.All list')
        if actual_done == '1':
            print(task_list['task'])
        elif actual_done == '2':
            print(task_list['completed'])
        else:
            print(task_list)
    elif choose == '5':
        print('Thanks and see you again')
        break
    else:
        print('input error\n try again')
        continue
