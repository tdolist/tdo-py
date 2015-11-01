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


def listundone(todolist):
    for key in todolist:
        print('\n## {name}\n'.format(name=key))
        for task_id in todolist[key]:
            if not todolist[key][task_id][1]:
                print('  [ ] {num} | {name}'
                      .format(num=task_id,
                              name=todolist[key][task_id][0]))
    print('\n', end='')


def listlists(todolist):
    print('You have the following todo lists:\n')
    for listname in todolist.keys():
        print('    [{undone}|{done}] {name}'.format(
            undone=get_undone(todolist[listname]),
            done=get_done(todolist[listname]), name=listname))
    print('\n', end='')


def get_undone(single_list):
    undone = 0
    for task_id in single_list:
        if not single_list[task_id][1]:
            undone += 1
    return undone


def get_done(single_list):
    done = 0
    for task_id in single_list:
        if single_list[task_id][1]:
            done += 1
    return done
