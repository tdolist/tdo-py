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
    settings = todolist.getsettings()
    globalid = 0
    try:
        globalid = settings['globalid']
    except TypeError as e:
        globalid = settings
        settings = {'globalid': globalid, 'table': False, 'tick': False}

    if len(argv) == 1:
        # tdo -- list undone todos
        todolist.listundone(todos, len(str(globalid - 1)), settings)
    elif argv[1] == 'all':
        # tdo all -- list ALL todos
        todolist.listall(todos, len(str(globalid - 1)), settings)
    elif argv[1] == 'add':
        if len(argv) < 3:
            displayhelp()
        # tdo add "itemname" [list]-- add a new item
        elif len(argv) < 4:
            # add to default list
            ret_val = todolist.add(todos, globalid, argv[2])
        else:
            # add to defined list
            ret_val = todolist.add(todos, globalid, argv[2], argv[3])

        if ret_val[1]:
            # if there were changes, save them
            todolist.save(ret_val[0])
            settings['globalid'] = ret_val[2]
            todolist.savesettings(settings)
    elif argv[1] == 'done':
        # tdo done x -- mark task no. x as done
        if len(argv) < 3:
            print('Please enter a task ID!')
        else:
            changed = False
            for element in argv[2:]:
                ret_val = todolist.done(todos, element)
                changed = changed or ret_val[1]

            if changed:
                # if there were changes, save them
                todolist.save(ret_val[0])
    elif argv[1] == 'edit':
        # tdo edit x - edit task no. x
        if len(argv) < 3:
            print('Please enter a task ID!')
        else:
            ret_val = todolist.edit(todos, argv[2])

            if ret_val[1]:
                # save changes, if there are any
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
    elif argv[1] == 'export':
        # tdo export filename -- export the todolist as markdown file
        if len(argv) < 3:
            print('You should provide a export filepath!')
        else:
            todolist.mdexport(todos)
    elif argv[1] == 'help':
        # tdo help -- display help
        displayhelp()
    elif argv[1] == 'themes':
        todolist.listthemes()
    elif argv[1] == 'settheme':
        settings = todolist.settheme(argv, settings)
        todolist.savesettings(settings)
    else:
        # something wrong? Help!
        displayhelp()


if __name__ == '__main__':
    main(sys.argv)
