import sys
from .listing import sortdict


def mdexport(todolist, exportfile):
    import os.path
    path = exportfile.rsplit('/', 1)[0]
    if not os.path.isdir(path):
        print('The given output path does not exist!')
    else:
        exportstring = '# Your todos:\n\n'
        if len(sys.argv) < 4:
            print('Exporting your todos to "{filename}"...'.format(
                filename=exportfile))
            keylist = sortdict(todolist)
            for key in keylist:
                exportstring += '## {listname}\n\n'.format(listname=key)
                idlist = sortdict(todolist[key], id=True)
                for todo_id in idlist:
                    exportstring += addtoexport(todolist[key][todo_id])
                exportstring += '\n'
            with open(exportfile, 'w') as f:
                f.write(exportstring)
            print('Done.')
        else:
            keylist = sys.argv[3:]
            notinlist = False
            for key in keylist:
                if key not in todolist:
                    print('You have no list named {nolist}'.format(nolist=key))
                    notinlist = True
            if notinlist:
                return
            else:
                for key in keylist:
                    exportstring += '## {listname}\n\n'.format(listname=key)
                    idlist = sortdict(todolist[key], id=True)
                    for todo_id in idlist:
                        exportstring += addtoexport(todolist[key][todo_id])
                    exportstring += '\n'
                print(exportstring)
                print('Done.')




def addtoexport(todolist):
        if todolist[1]:
            done = 'x'
        else:
            done = ' '
        return'  - [{done}] {todoname}\n'.format(
            done=done,
            todoname=todolist[0])
