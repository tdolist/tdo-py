def listall(todolist):
    for key in todolist:
        print('\n## {name}\n'.format(name=key))
        for task_id in todolist[key]:
            if todolist[key][task_id][1]:
                done = 'x'
            else:
                done = ' '

            print('  [{done}] {num} | {name}'
                  .format(done=done, num=task_id,
                          name=todolist[key][task_id][0]))
    print('\n', end='')
