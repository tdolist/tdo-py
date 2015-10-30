def add(todolist, todoname, category='all'):
    if category not in todolist.keys():
        print('There is no todo list with the name {name}.'
              .format(name=category))
        return todolist, False

    print('Adding {nam} to category \'{cat}\'.'.format(nam=todoname,
                                                       cat=category))
    todoid = 1
    todolist[category][todoid] = [todoname, False]
    print(todolist)
    return todolist, True
