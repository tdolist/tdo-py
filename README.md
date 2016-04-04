# > tdo

[![License](https://img.shields.io/badge/license-MIT-red.svg?style=flat
            )](http://mit-license.org)
[![Language](https://img.shields.io/badge/language-Python%203.5%2B-blue.svg
            )](https://www.python.org)
[![Release](https://img.shields.io/badge/release-v1.1.3-brightgreen.svg
            )](https://github.com/tdolist/tdo/releases/latest)
[![Build Status](https://travis-ci.org/tdolist/tdo.svg?branch=master
            )](https://travis-ci.org/tdolist/tdo)


A todo list tool for the terminal, written in Python.

![tdo](https://cloud.githubusercontent.com/assets/6068259/11023461/b922d256-8679-11e5-8d27-299fa328763f.gif)

This is a simple todo list tool that integrates in your terminal workflow.  
Featuring multiple todo lists and exporting your list to Markdown, it aims to be a well-structured assistant in your daily routine when you don't feel like leaving the terminal.

## Installation

You can install tdo via _pip for Python3_, using  
```
pip3 install tdo
```

For a manual installation, download the [latest release](https://github.com/tdolist/tdo/releases/latest) and run
```
sudo ./setup.py install
```

However, to __uninstall__ it you will still need pip and have to run
```
pip3 uninstall tdo
```

## Usage

__Notice:__ If you have todos or listnames with spaces do not forget to escape them or put the whole string in `''`

For a list of all available commands please see `tdo help`, this is just an overview to demonstrate what you can do with tdo.

### Simple todos
To add a todo, simply type `tdo add 'todo goes here'`. If your todo consists of just one word, you can leave out the quotes.

However, if you want to add the todo to a list _(for lists, see below)_, type `tdo add 'todo' listname`. Note that you can type the listname in lowercase letters, tdo will still find your list.

### Multiple Lists
tdo features working with multiple lists. Add a new list with `tdo newlist listname` (remember to use quotation marks for a listname containing spaces!).

To remove it again, use `tdo remove listname`. You will be prompted to confirm the deletion to avoid accidents.

### Theming
tdo features a set of four different themes, where two are based on a table-like structure and the other two are more plain-structured.
You can preview all available themes using `tdo themes` but you shouldn't expect too much, it's still the terminal. Simple is cool here.  

If you feel like changing your theme, you can do that with `tdo settheme <Theme ID goes here>`.

### Export your todos
If you feel like exporting your todos _(e.g. for printing a checklist)_, you can do that with `tdo export filename`. All your todo lists will be exported, including tasks that were marked as 'done'.

## License

This work is published under the [MIT License](LICENSE.txt).
