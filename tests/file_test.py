import unittest
from tdo import todolist
from unittest.mock import patch


class FileTest(unittest.TestCase):

    def setUp(self):
        todolist.load()
        todolist.getsettings()

    def test_one(self):
        from os.path import exists
        self.assertTrue(exists(todolist.jsonfile),
                        msg='The todo list JSON file has not been created!')
        self.assertTrue(exists(todolist.settingsfile),
                        msg='The settings JSON file has not been created!')

    @patch('builtins.input', lambda x: 'yes')
    def test_two(self):
        from tdo import main

        todolist.reset()
        fake_argv = ['../tdo.py', 'add', 'Test1']
        main(fake_argv)
        fake_argv = ['../tdo.py', 'add', 'Test2']
        main(fake_argv)
        fake_argv = ['../tdo.py', 'add', 'Test3']
        main(fake_argv)

        self.assertEqual(todolist.getsettings()['globalid'], 4,
                         msg='The global todo ID incrementation is broken \
(The settings file contains a wrong ID).')
        todos = todolist.load()
        self.assertEqual(len(todos['default']), 3,
                         msg='There were not enough/too much entries in lists.\
json.')
