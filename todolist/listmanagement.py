def add(todolist, todoid, todoname, category='all'):
    if category not in todolist.keys():
        print('There is no todo list with the name {name}.'
              .format(name=category))
        return todolist, False

    print('Adding {nam} to category \'{cat}\'.'.format(nam=todoname,
                                                       cat=category))
    todolist[category][todoid] = [todoname, False]
    print(todolist)
    todoid += 1
    return todolist, True, todoid


def done(todolist, task_id):
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
    if new_category in todolist.keys():
        print('This list already exists!')
        return todolist, False
    else:
        todolist[new_category] = {}
        return todolist, True


def dellist(tasklist, listname, get_undone, get_done):

    if listname not in tasklist:
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
            return tasklist, True
        else:
            return tasklist, False
