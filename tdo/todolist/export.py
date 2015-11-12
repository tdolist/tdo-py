from .listing import sortdict


def mdexport(todolist, exportfile):
    import os.path
    path = exportfile.rsplit('/', 1)[0]
    if not os.path.isdir(path):
        print('The given output path does not exist!')
    else:
        print('Exporting your todos to "{filename}"...'.format(
            filename=exportfile))
        exportstring = '# Your todos:\n\n'
        keylist = sortdict(todolist)
        for key in keylist:
            exportstring += '## {listname}\n\n'.format(listname=key)
            idlist = sortdict(todolist[key], id=True)
            for todo_id in idlist:
                if todolist[key][todo_id][1]:
                    done = 'x'
                else:
                    done = ' '
                exportstring += '  - [{done}] {todoname}\n'.format(
                    done=done,
                    todoname=todolist[key][todo_id][0])
            exportstring += '\n'
        with open(exportfile, 'w') as f:
            f.write(exportstring)
        print('Done.')
