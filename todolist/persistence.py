import json
import os

home = os.environ['HOME']
jsonfile = '{home}/.tdo/list.json'.format(home=home)
settingsfile = '{home}/.tdo/settings.json'.format(home=home)


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
