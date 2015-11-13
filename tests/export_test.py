import unittest
from tdo import main, todolist
from unittest.mock import patch


class FileTest(unittest.TestCase):

    @patch('builtins.input', lambda x: 'yes')
    def setUp(self):
        todolist.reset()
        fake_argv = ['../tdo.py', 'add', 'Test1']
        main(fake_argv)
        fake_argv = ['../tdo.py', 'add', 'Test2']
        main(fake_argv)
        fake_argv = ['../tdo.py', 'add', 'Test3']
        main(fake_argv)
        fake_argv = ['../tdo.py', 'newlist', 'Testlist1']
        main(fake_argv)
        fake_argv = ['../tdo.py', 'add', 'Test1', 'Testlist1']
        main(fake_argv)
        fake_argv = ['../tdo.py', 'add', 'Test2', 'Testlist1']
        main(fake_argv)
        fake_argv = ['../tdo.py', 'add', 'Test3', 'Testlist1']
        main(fake_argv)
        fake_argv = ['../tdo.py', 'newlist', 'Testlist2']
        main(fake_argv)
        fake_argv = ['../tdo.py', 'add', 'Test1', 'Testlist2']
        main(fake_argv)
        fake_argv = ['../tdo.py', 'add', 'Test2', 'Testlist2']
        main(fake_argv)
        fake_argv = ['../tdo.py', 'add', 'Test3', 'Testlist2']
        main(fake_argv)

    def test_alllists(self):
        fake_argv = ['../tdo.py', 'export', './test.md']
        todos = todolist.load()
        todolist.mdexport(todos, fake_argv)
        shouldstr = '''# Your todos:

## default

  - [ ] Test1
  - [ ] Test2
  - [ ] Test3

## Testlist1

  - [ ] Test1
  - [ ] Test2
  - [ ] Test3

## Testlist2

  - [ ] Test1
  - [ ] Test2
  - [ ] Test3

'''
        isstr = ''
        with open('./test.md') as mdfile:
            isstr = mdfile.read()

        self.assertEqual(shouldstr, isstr, msg='Can not export all lists.')

    def test_sinlgelist(self):
        fake_argv = ['../tdo.py', 'export', './test.md', 'Testlist1']
        todos = todolist.load()
        todolist.mdexport(todos, fake_argv)
        shouldstr = '''# Your todos:

## Testlist1

  - [ ] Test1
  - [ ] Test2
  - [ ] Test3

'''
        isstr = ''
        with open('./test.md') as mdfile:
            isstr = mdfile.read()

        self.assertEqual(shouldstr, isstr, msg='Can not export all lists.')

    def test_multilist(self):
        fake_argv = ['../tdo.py', 'export', './test.md', 'Testlist1',
                     'Testlist2']
        todos = todolist.load()
        todolist.mdexport(todos, fake_argv)
        shouldstr = '''# Your todos:

## Testlist1

  - [ ] Test1
  - [ ] Test2
  - [ ] Test3

## Testlist2

  - [ ] Test1
  - [ ] Test2
  - [ ] Test3

'''
        isstr = ''
        with open('./test.md') as mdfile:
            isstr = mdfile.read()

        self.assertEqual(shouldstr, isstr, msg='Can not export all lists.')
