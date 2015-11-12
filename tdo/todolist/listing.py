from .printing import *


def listall(todolist, num_len, settings):
    '''
    Lists all todos from all categories, even the ones marked as "done".
    Takes:
        - the todolist dict
        - the length of the longest Todo-ID (for formatting)
        - the settings
    Returns:
        nothing
    '''
    table = settings['table']
    tick = settings['tick']
    if table:
        printhead(num_len)
    keylist = sortdict(todolist)
    for key in keylist:
        # print the category name
        printtitle(key, table, num_len)
        if len(todolist[key]) == 0:
            print('    No entries found.')
        else:
            idlist = sortdict(todolist[key], id=True)
            for task_id in idlist:
                # prints the todo
                printtask(done=todolist[key][task_id][1], num_len=num_len,
                          task_id=task_id, name=todolist[
                          key][task_id][0], table=table, tick=tick)
        print('\n', end='')
    print('\n', end='')


def listundone(todolist, num_len, settings):
    '''
    Lists all undone todos by category.
    Takes:
        - the todolist dict
        - the length of the longest Todo-ID (for formatting)
        - the settings
    Returns:
        nothing
    '''
    table = settings['table']
    tick = settings['tick']
    keylist = sortdict(todolist)
    if table:
        printhead(num_len)
    for key in keylist:
        printtitle(key, table, num_len)
        if len(todolist[key]) == 0:
            print('    No entries found.')
        else:
            undone = False
            idlist = sortdict(todolist[key], id=True)
            for task_id in idlist:
                if not todolist[key][task_id][1]:
                    undone = True
                    printtask(num_len=num_len, task_id=task_id,
                              name=todolist[key][task_id][0], table=table,
                              tick=tick)
            if not undone:
                print('    No undone tasks.')
    print('\n', end='')


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
        print('    [\033[91m{undone}\033[0m|\033[92m{done}\033[0m] \
{name}'.format(
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


def sortdict(todolist, id=False):
    if id:
        todolist = [int(x) for x in todolist]
    templist = sorted(todolist)
    ret_list = []
    if not id:
        templist.remove('default')
        ret_list.append('default')
    for element in templist:
        ret_list.append(str(element))
    return ret_list
