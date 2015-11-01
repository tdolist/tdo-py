#!/usr/bin/env python3

import sys
import todolist


todos = {}
globalid = 0


def main():
    global todos
    todos = todolist.load()
    globalid = todolist.getsettings()

    print(sys.argv)
    if len(sys.argv) == 1:
        todolist.listundone(todos)
    elif sys.argv[1] == 'all':
        todolist.listall(todos)
    elif sys.argv[1] == 'add':
        print('Let me add this...')
        if len(sys.argv) < 4:
            ret_val = todolist.add(todos, globalid, sys.argv[2])
        else:
            ret_val = todolist.add(todos, globalid, sys.argv[2], sys.argv[3])
        if ret_val[1]:
            todolist.save(ret_val[0])
            todolist.savesettings(ret_val[2])
    elif sys.argv[1] == 'done':
        if len(sys.argv) < 3:
            print('Please enter a task ID!')
        else:
            ret_val = todolist.done(todos, sys.argv[2])

            if ret_val[1]:
                todolist.save(ret_val[0])
    elif sys.argv[1] == 'newlist':
        if len(sys.argv) < 3:
            print('Please enter a name for your new list!')
        else:
            ret_val = todolist.addlist(todos, sys.argv[2])

            if ret_val[1]:
                todolist.save(ret_val[0])
    elif sys.argv[1] == 'remove':
        if len(sys.argv) < 3:
            print('Please enter a list that should be deleted!')
        else:
            ret_val = todolist.dellist(todos, sys.argv[2], todolist.get_undone,
                                       todolist.get_done)

            if ret_val[1]:
                todolist.save(ret_val[0])
    elif sys.argv[1] == 'clean':
        if len(sys.argv) < 3:
            # clean all lists
            ret_val = todolist.clean(todos)
        else:
            # only clean a single list
            ret_val = todolist.clean(todos, sys.argv[2])

        if ret_val[1]:
            todolist.save(ret_val[0])
    elif sys.argv[1] == 'lists':
        todolist.listlists(todos)
    elif sys.argv[1] == 'help':
        todolist.help()
    else:
        todolist.help()


if __name__ == '__main__':
    main()
