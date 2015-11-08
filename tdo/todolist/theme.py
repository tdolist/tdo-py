from .listing import listall
import json

num_len = 1
examplelist = {'default': {
    '1': ['This is an example', False], '2': ['This one is done', True]}}
tempsettings = {'globalid': 1, 'table': False, 'tick': False}


def listthemes():
    print('\033[1m\033[91mTheme 1:\033[0m')
    listall(examplelist, num_len, tempsettings)
    print('\033[1m\033[91mTheme 2:\033[0m')
    tempsettings['tick'] = True
    listall(examplelist, num_len, tempsettings)
    print('\033[1m\033[91mTheme 3:\033[0m')
    tempsettings['tick'] = False
    tempsettings['table'] = True
    listall(examplelist, num_len, tempsettings)
    print('\033[1m\033[91mTheme 4:\033[0m')
    tempsettings['tick'] = True
    listall(examplelist, num_len, tempsettings)


def settheme(argv, settings):
    if len(argv) < 3:
        print('You have to select a theme.\nYou can get a list of all themes \
with "themes"')
    elif argv[2] == '1':
        settings['tick'] = False
        settings['table'] = False
    elif argv[2] == '2':
        settings['tick'] = True
        settings['table'] = False
    elif argv[2] == '3':
        settings['tick'] = False
        settings['table'] = True
    elif argv[2] == '4':
        settings['tick'] = True
        settings['table'] = True
    else:
        print('There is no theme {id}.\nYou can get a list of all themes \
with "themes"'.format(id=argv[2]))
    return settings
