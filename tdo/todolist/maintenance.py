import os
import re
import json
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
            globalid = 1
            json.dump(globalid, f, indent=4)

        print('Alright, your todo lists have been cleared.')
    elif answer == 'no':
        print('Okay, let\'s keep your lists for a while.')
    else:
        print('Please write "yes" or "no".')


def update():
    os.chdir(os.path.join(home + '/.tdo'))
    user = 'Feliix42'
    repo = 'tdo'
    output = subprocess.getoutput('curl -s https://api.github.com/repos/\
{user}/{repo}/releases'.format(user=user, repo=repo))
    linklist = re.search(r'"browser_download_url": "(https\:\/\/.*\.zip)"',
                         output)
    try:
        link = linklist.group(1)
        with urllib.request.urlopen(link) as resp, open('download.zip', 'wb') as f:
            data = resp.read()
            f.write(data)
        import zipfile
        with zipfile.ZipFile('download.zip', "r") as z:
            z.extractall(".")
    except AttributeError:
        print('No release available')
