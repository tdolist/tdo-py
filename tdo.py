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
        ret_val = todolist.done(todos, sys.argv[2])

        if ret_val[1]:
            todolist.save(ret_val[0])
    elif sys.argv[1] == 'help':
        todolist.help()
    else:
        todolist.help()


if __name__ == '__main__':
    main()
