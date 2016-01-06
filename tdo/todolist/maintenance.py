import os
import re
import json
import shutil
import subprocess
import urllib.request
from .persistence import home, jsonfile, settingsfile


def reset():
    '''
    Resets all data to presets. Prompts the user for confirmation.
    Takes:
        nothing
    Returns:
        nothing
    '''

    answer = input('Are you sure you want to reset all todo lists? (yes/no) ')
    if answer == 'yes':

        with open(jsonfile, 'w') as f:
            json.dump({'default': {}}, f, indent=4)

        with open(settingsfile, 'w') as f:
            settings = {'globalid': 1, 'table': False, 'tick': False}
            json.dump(settings, f, indent=4)

        print('Alright, your todo lists have been cleared.')
    elif answer == 'no':
        print('Okay, let\'s keep your lists for a while.')
    else:
        print('Please write "yes" or "no".')
