import os


_, columns = os.popen('stty size', 'r').read().split()
columns = int(columns)


def printhead(num_len):
    spaces = 0 if (num_len - 5) <= 0 else round((num_len - 5) / 2)
    headline = 'Done |{space}  ID  {space}| Task'.format(space=' ' * spaces)
    print(headline)
    printhline(2 * spaces)


def printtitle(title, table, num_len):
    if table:
        spaces = 0 if (num_len - 5) <= 0 else round((num_len - 5) / 2)
        tileline = '\033[1m{title}\033[0m'.format(title=title)
        print(tileline)
        printhline(2 * spaces)
    else:
        print('## {title}'.format(title=title))


def printtask(num_len, task_id, name, table, tick, done=False):
    donestr = ''
    tasklist = []
    spaces = 0 if (num_len - 5) <= 0 else round((num_len - 5) / 2)
    printedId = print_id(num_len, task_id)
    maxLen = 0
    if table:
        maxLen = 12 if spaces == 0 else 13 + spaces
    else:
        maxLen = 8 if spaces == 0 else 13 + spaces
    if len(name) > maxLen:
        for entry in list(split_by_n(name, (columns - maxLen - 2))):
            tasklist.append(entry)
    else:
        tasklist.append(name)
    if tick:
        donestr = ' \033[92m\u2714\033[0m ' if done else '   '
    else:
        donestr = '[x]' if done else '[ ]'

    if table:
        space = (5 - num_len) if spaces == 0 else spaces
        print(' {done} |{space}{id} | {task}'.format(done=donestr,
                                                     space=' ' * space,
                                                     id=printedId,
                                                     task=tasklist[0]))
        if len(tasklist) > 1:
            for element in range(len(tasklist) - 1):
                print('     |{idlen}| {task}'.format(idlen=' ' * (maxLen - 6),
                                                     task=tasklist[element + 1])
                      )
    else:
        print('  {done} {num} | {name}'
              .format(done=donestr, num=print_id(num_len, task_id),
                      name=tasklist[0]))
        if len(tasklist) > 1:
            for element in range(len(tasklist) - 1):
                print('{idlen}| {task}'.format(idlen=' ' * maxLen,
                                               task=tasklist[element + 1]))


def print_id(num_len, task_id):
    '''
    Calculates how much spaces need to be added for formatting purposes.
    Takes:
        - the length of the longest Todo-ID (for formatting)
        - the specific task id (as String!)
    Returns:
        a formatted String like "   2".
    '''
    return ' ' * (num_len - len(task_id)) + task_id


def printhline(addition):
    print('=====\u01C2{idspace}\u01C2{fill}'.format(
        idspace='=' * (addition + 6), fill='=' * (columns - 13 - addition)))


def split_by_n(seq, n):
    while seq:
        yield seq[:n]
        seq = seq[n:]
