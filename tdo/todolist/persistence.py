import json
import os

home = os.environ['HOME']
jsonfile = '{home}/.tdo/list.json'.format(home=home)
settingsfile = '{home}/.tdo/settings.json'.format(home=home)


def save(todolist):
    with open(jsonfile, 'w') as backupfile:
        json.dump(todolist, backupfile, indent=4)


def load():
    try:
        with open(jsonfile, 'r') as backupfile:
            return json.load(backupfile)
    except FileNotFoundError:
        os.makedirs(os.path.dirname(jsonfile), exist_ok=True)
        initdict = {'all': {}}
        with open(jsonfile, 'w') as f:
            json.dump(initdict, f)
        return initdict


def savesettings(globalid):
    with open(settingsfile, 'w') as settings:
        json.dump(globalid, settings, indent=4)


def getsettings():
    try:
        with open(settingsfile, 'r') as settings:
            return json.load(settings)
    except FileNotFoundError:
        os.makedirs(os.path.dirname(settingsfile), exist_ok=True)
        with open(settingsfile, 'w') as f:
            globalid = 1
            json.dump(globalid, f, indent=4)
            return globalid
