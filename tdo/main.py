#!/usr/bin/env python3

import sys
from . import todolist


# the todo lists dict
todos = {}
# the global ID counter
globalid = 0


def displayhelp():
    '''
    Display the help page.
    '''
    print(todolist.help)


def main(argv=sys.argv):
    # initialize the program by loading settings and
    global todos
    todos = todolist.load()
    globalid = todolist.getsettings()

    if len(argv) == 1:
        # tdo -- list undone todos
        todolist.listundone(todos, len(str(globalid - 1)))
    elif argv[1] == 'all':
        # tdo all -- list ALL todos
        todolist.listall(todos, len(str(globalid - 1)))
    elif argv[1] == 'add':
        # tdo add "itemname" [list]-- add a new item
        if len(argv) < 4:
            # add to default list
            ret_val = todolist.add(todos, globalid, argv[2])
        else:
            # add to defined list
            ret_val = todolist.add(todos, globalid, argv[2], argv[3])

        if ret_val[1]:
            # if there were changes, save them
            todolist.save(ret_val[0])
            todolist.savesettings(ret_val[2])
    elif argv[1] == 'done':
        # tdo done x -- mark task no. x as done
        if len(argv) < 3:
            print('Please enter a task ID!')
        else:
            ret_val = todolist.done(todos, argv[2])

            if ret_val[1]:
                # if there were changes, save them
                todolist.save(ret_val[0])
    elif argv[1] == 'newlist':
        # tdo newlist "name" -- create list "name"
        if len(argv) < 3:
            print('Please enter a name for your new list!')
        else:
            ret_val = todolist.addlist(todos, argv[2])

            if ret_val[1]:
                todolist.save(ret_val[0])
    elif argv[1] == 'remove':
        # tdo remove "name" -- delete the list named "name"
        if len(argv) < 3:
            print('Please enter a list that should be deleted!')
        else:
            ret_val = todolist.dellist(todos, argv[2], todolist.get_undone,
                                       todolist.get_done)

            if ret_val[1]:
                todolist.save(ret_val[0])
    elif argv[1] == 'clean':
        # tdo clean [list] -- remove done taks from one/all list(s)
        if len(argv) < 3:
            # clean all lists
            ret_val = todolist.clean(todos)
        else:
            # only clean a single list
            ret_val = todolist.clean(todos, argv[2])

        if ret_val[1]:
            todolist.save(ret_val[0])
    elif argv[1] == 'reset':
        # tdo reset -- reset your settings and todos and todo lists
        todolist.reset()
    elif argv[1] == 'lists':
        # tdo lists -- list all todo lists
        todolist.listlists(todos)
    elif argv[1] == 'help':
        # tdo help -- display help
        displayhelp()
    elif argv[1] == 'update':
        todolist.update()
    else:
        # something wrong? Help!
        displayhelp()


if __name__ == '__main__':
    main(sys.argv)
