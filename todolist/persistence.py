import json

jsonfile = '/Users/Felix/.tdo/list.json'
settingsfile = '/Users/Felix/.tdo/settings.json'


def save(todolist):
    with open(jsonfile, 'w') as backupfile:
        json.dump(todolist, backupfile, indent=4)


def load():
    with open(jsonfile, 'r') as backupfile:
        return json.load(backupfile)


def savesettings(globalid):
    with open(settingsfile, 'w') as settings:
        json.dump(globalid, settings, indent=4)


def getsettings():
    with open(settingsfile, 'r') as settings:
        return json.load(settings)
