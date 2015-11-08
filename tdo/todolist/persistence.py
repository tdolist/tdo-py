import json
import os

# file paths for the settings and the todolist file
home = os.environ['HOME']
jsonfile = '{home}/.tdo/list.json'.format(home=home)
settingsfile = '{home}/.tdo/settings.json'.format(home=home)


def save(todolist):
    '''
    Dumps the todo lists to the default JSON file, nicely indented and
    human readable.
    Takes:
        - todolist dict
    Returns:
        nothing
    '''
    with open(jsonfile, 'w') as backupfile:
        json.dump(todolist, backupfile, indent=4)


def load():
    '''
    Loads the todo lists from the default JSON file. If this is not existing
    it will be created and initialized.
    Takes:
        nothing
    Returns:
        the todolist dict (from a previous session)
    '''
    try:
        with open(jsonfile, 'r') as backupfile:
            return json.load(backupfile)
    except FileNotFoundError:
        os.makedirs(os.path.dirname(jsonfile), exist_ok=True)
        initdict = {'default': {}}
        with open(jsonfile, 'w') as f:
            json.dump(initdict, f)
        return initdict


def savesettings(settings):
    '''
    Dumps the todo list settings to the default JSON file.
    Takes:
        - global ID counter
    Returns:
        nothing
    '''
    with open(settingsfile, 'w') as settingsf:
        json.dump(settings, settingsf, indent=4)


def getsettings():
    '''
    Loads the todo list settings from the default JSON file.
    If this is not existing it will be created and initialized.
    Takes:
        nothing
    Returns:
        the global ID counter (from a previous session)
    '''
    try:
        with open(settingsfile, 'r') as settings:
            return json.load(settings)
    except FileNotFoundError:
        os.makedirs(os.path.dirname(settingsfile), exist_ok=True)
        with open(settingsfile, 'w') as f:
            settings = {'globalid': 1, 'table': False, 'tick': False}
            json.dump(settings, f, indent=4)
            return settings
