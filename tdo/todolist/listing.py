def listall(todolist, num_len):
    '''
    Lists all todos from all categories, even the ones marked as "done".
    Takes:
        - the todolist dict
        - the length of the longest Todo-ID (for formatting)
    Returns:
        nothing
    '''
    for key in todolist:
        # print the category name
        print('## {name}'.format(name=key))
        if len(todolist[key]) == 0:
            print('    No entries found.')
        else:
            for task_id in todolist[key]:
                if todolist[key][task_id][1]:
                    done = 'x'
                else:
                    done = ' '

                # prints the todo
                print('  [{done}] {num} | {name}'
                      .format(done=done, num=print_id(num_len, task_id),
                              name=todolist[key][task_id][0]))
        print('\n', end='')
    print('\n', end='')


def listundone(todolist, num_len):
    '''
    Lists all undone todos by category.
    Takes:
        - the todolist dict
        - the length of the longest Todo-ID (for formatting)
    Returns:
        nothing
    '''
    for key in todolist:
        print('\n## {name}'.format(name=key))
        if len(todolist[key]) == 0:
            print('    No entries found.')
        else:
            undone = False
            for task_id in todolist[key]:
                if not todolist[key][task_id][1]:
                    undone = True
                    print('  [ ] {num} | {name}'
                          .format(num=print_id(num_len, task_id),
                                  name=todolist[key][task_id][0]))
            if not undone:
                print('    No undone tasks.')
    print('\n', end='')


def print_id(num_len, task_id):
    '''
    Calculates how much spaces need to be added for formatting purposes.
    Takes:
        - the length of the longest Todo-ID (for formatting)
        - the specific task id (as String!)
    Returns:
        a formatted String like "   2".
    '''
    return ' ' * (num_len - len(task_id)) + task_id


def listlists(todolist):
    '''
    Lists all lists and how much undone and done tasks they contain.
    Takes:
        - the todolist dict
    Returns:
        nothing
    '''
    print('You have the following todo lists:\n')
    for listname in todolist.keys():
        print('    [{undone}|{done}] {name}'.format(
            undone=get_undone(todolist[listname]),
            done=get_done(todolist[listname]), name=listname))
    print('\n', end='')


def get_undone(single_list):
    '''
    Returns the number of undone tasks in a list.
    Takes:
        - a single todo list
    Returns:
        the number of undone tasks from that list
    '''
    undone = 0
    for task_id in single_list:
        if not single_list[task_id][1]:
            undone += 1
    return undone


def get_done(single_list):
    '''
    Returns the number of tasks in the list, that have been marked as "done".
    Takes:
        - a single todo list
    Returns:
        the number of undone tasks from that list
    '''
    done = 0
    for task_id in single_list:
        if single_list[task_id][1]:
            done += 1
    return done
