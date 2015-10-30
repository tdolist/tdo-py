import json

jsonfile = '/Users/Felix/.tdo/list.json'


def save(todolist):
    with open(jsonfile, 'w') as backupfile:
        json.dump(todolist, backupfile)


def load():
    with open(jsonfile, 'r') as backupfile:
        return json.load(backupfile)
