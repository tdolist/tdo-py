def add(tasklist, todoid, todoname, category='all'):
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


def done(tasklist, task_id):
    changed = False
    found = False
    for category in tasklist:
        for i in tasklist[category]:
            if i == str(task_id):
                found = True
                if tasklist[category][i][1]:
                    print('This task has already been marked as completed!')
                else:
                    tasklist[category][i][1] = True
                    changed = True
                    print('Task #{number} has been marked as completed.'
                          .format(number=task_id))
    if not found:
        print('There is no task with the ID {num}.'.format(num=task_id))
        return tasklist, False
    else:
        if changed:
            return tasklist, True
        else:
            return tasklist, False
