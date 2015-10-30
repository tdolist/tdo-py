def listall(todolist):
    for key in todolist:
        print('\n## {name}\n'.format(name=key))
        for task_id in todolist[key]:
            if todolist[key][task_id][1]:
                done = 'x'
            else:
                done = ' '

            print('  [{done}] {name}'.format(done=done,
                                             name=todolist[key][task_id][0]))
    print('\n', end='')
