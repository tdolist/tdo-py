help = '''tdo -- A todo list tool for the terminal.

Available commands:
tdo                     Lists all undone tasks, sorted by category.
tdo all                 Lists all tasks.
tdo add "task" [list]   Add a task to a certain list or the default list.
tdo edit id             Edit a task description.
tdo done id             Mark tha task with the ID 'id' as done.
tdo newlist "name"      Create a new list named 'name'
tdo remove "list"       Delete the list 'list'
tdo clean [list]        Removes all tasks that have been marked as done.
                        If you specify a list name, only this list is cleared.
tdo lists               List all lists with a statistic of undone/done tasks.
tdo help                Display this help.
tdo reset               DANGER ZONE. Delete all your todos and todo lists.
tdo themes              Shows all available themes.
tdo settheme id         Set the theme to <id>
tdo export filename     Export all your todos to Markdown.'''
