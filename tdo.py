#!/usr/bin/env python3

import sys
import todolist


todos = {}


def main():
    global todos
    todos = todolist.load()

    print(sys.argv)
    if len(sys.argv) == 1:
        todolist.listall(todos)
    elif sys.argv[1] == 'add':
        print('Let me add this.')
        if len(sys.argv) < 4:
            ret_val = todolist.add(todos, sys.argv[2])
        else:
            ret_val = todolist.add(todos, sys.argv[2], sys.argv[3])
        if ret_val[1]:
            todos = ret_val[0]
            todolist.save(todos)

    else:
        print('Standardfall: Hilfe öffnen')


if __name__ == '__main__':
    main()
