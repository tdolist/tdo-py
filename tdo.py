#!/usr/bin/env python3

import sys
import todolist


todos = {}
globalid = 0


def displayhelp():
    with open('todolist/help', 'r') as helpfile:
        print(helpfile.read())


def main(argv):
    global todos
    todos = todolist.load()
    globalid = todolist.getsettings()

    # print(argv)
    if len(argv) == 1:
        todolist.listundone(todos)
    elif argv[1] == 'all':
        todolist.listall(todos)
    elif argv[1] == 'add':
        print('Let me add this...')
        if len(argv) < 4:
            ret_val = todolist.add(todos, globalid, argv[2])
        else:
            ret_val = todolist.add(todos, globalid, argv[2], argv[3])
        if ret_val[1]:
            todolist.save(ret_val[0])
            todolist.savesettings(ret_val[2])
    elif argv[1] == 'done':
        if len(argv) < 3:
            print('Please enter a task ID!')
        else:
            ret_val = todolist.done(todos, argv[2])

            if ret_val[1]:
                todolist.save(ret_val[0])
    elif argv[1] == 'newlist':
        if len(argv) < 3:
            print('Please enter a name for your new list!')
        else:
            ret_val = todolist.addlist(todos, argv[2])

            if ret_val[1]:
                todolist.save(ret_val[0])
    elif argv[1] == 'remove':
        if len(argv) < 3:
            print('Please enter a list that should be deleted!')
        else:
            ret_val = todolist.dellist(todos, argv[2], todolist.get_undone,
                                       todolist.get_done)

            if ret_val[1]:
                todolist.save(ret_val[0])
    elif argv[1] == 'clean':
        if len(argv) < 3:
            # clean all lists
            ret_val = todolist.clean(todos)
        else:
            # only clean a single list
            ret_val = todolist.clean(todos, argv[2])

        if ret_val[1]:
            todolist.save(ret_val[0])
    elif argv[1] == 'lists':
        todolist.listlists(todos)
    elif argv[1] == 'help':
        displayhelp()
    else:
        displayhelp()


if __name__ == '__main__':
    main(sys.argv)
