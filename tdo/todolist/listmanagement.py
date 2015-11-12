def add(todolist, todoid, todoname, category='default'):
    '''
    Adds a new item to a todo list.
    Takes:
        - the todolist dict
        - the next free todo-ID
        - the name of the todo
        - a category (this is optional)
    Returns:
        the (updated) todolist dict, False for no changes/True for changes &
        the next free ID
    '''
    if category not in todolist.keys():
        print('There is no todo list with the name {name}.'
              .format(name=category))
        return todolist, False, todoid
    elif todoname == '':
        print('You definitely should name your todo!')
        return todolist, False, todoid

    print('Adding "{nam}" to category \'{cat}\'.'.format(nam=todoname,
                                                         cat=category))
    todolist[category][todoid] = [todoname, False]
    todoid += 1
    return todolist, True, todoid


def done(todolist, task_id):
    '''
    Marks an item as done.
    Takes:
        - the todolist dict
        - the task id that should be marked as done
    Returns:
        the (updated) todolist dict, False for no changes/True for changes
    '''
    changed = False
    found = False
    for category in todolist:
        for i in todolist[category]:
            if i == str(task_id):
                found = True
                if todolist[category][i][1]:
                    print('This task has already been marked as completed!')
                else:
                    todolist[category][i][1] = True
                    changed = True
                    print('Task #{number} has been marked as completed.'
                          .format(number=task_id))
    if not found:
        print('There is no task with the ID {num}.'.format(num=task_id))
        return todolist, False
    else:
        if changed:
            return todolist, True
        else:
            return todolist, False


def addlist(todolist, new_category):
    '''
    Adds a new todo list.
    Takes:
        - the todolist dict
        - the name of the new category
    Returns:
        the (updated) todolist dict, False for no changes/True for changes
    '''
    if new_category in todolist.keys():
        print('This list already exists!')
        return todolist, False
    else:
        todolist[new_category] = {}
        return todolist, True


def dellist(tasklist, listname, get_undone, get_done):
    '''
    Deletes a todo list. Prompts the user to confirm his actions.
    Takes:
        - the todolist dict
        - the name of the todo list
        - the function to get the number of undone tasks
        - the function to get the number of done tasks
    Returns:
        the (updated) todolist dict, False for no changes/True for changes
    '''
    if listname == 'default':
        print('You may not delete the default list.')
    elif listname not in tasklist:
        print('There is no list with the name "{name}"!'.format(name=listname))
        return tasklist, False
    else:
        answer = ''
        while answer not in ['yes', 'no']:
            answer = input('Your list "{name}" contains {undone} and {done} tasks.\n\
Are you sure you want to delete it? (yes/no) '.format(
                name=listname,
                undone=get_undone(tasklist[listname]),
                done=get_done(tasklist[listname])))
        if answer == 'yes':
            del tasklist[listname]
            print('List deleted.')
            return tasklist, True
        else:
            return tasklist, False


def clean(todolist, cat=''):
    '''
    Removes every todo from all lists/one single list, that has been marked as
    "done".
    Takes:
        - the todolist dict
        - (optional: a category)
    Returns:
        the (cleaned) todolist dict, False for no changes/True for changes
    '''
    deleted = 0
    if cat == '':
        for category in todolist:
            todolist[category] = {task_id: todolist[category][
                task_id] for task_id in todolist[category] if not todolist[
                category][task_id][1]}
        return todolist, True
    else:
        if cat not in todolist.keys():
            print('This list does not exist.')
            return todolist, False
        else:
            todolist[cat] = {task_id: todolist[cat][task_id]
                             for task_id in todolist[cat] if not todolist[cat][
                             task_id][1]}
            return todolist, True
