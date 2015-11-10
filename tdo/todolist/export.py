def mdexport(todolist, exportfile):
    import os.path
    path = exportfile.rsplit('/', 1)[0]
    if not os.path.isdir(path):
        print('The given output path does not exist!')
    else:
        print('Exporting your todos to "{filename}"...'.format(
            filename=exportfile))
        exportstring = '# Your todos:\n\n'
        for key in todolist:
            # TODO add sorting
            exportstring += '## {listname}\n\n'.format(listname=key)
            for todo_id in todolist[key]:
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
