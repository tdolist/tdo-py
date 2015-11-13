import unittest
import subprocess


class UpdateTest(unittest.TestCase):

    def test_one(self):
        try:
            subprocess.call(['tdo'])
            subprocess.call(['../setup.py', 'uninstall'])
        except Exception as err:
            pass
        finally:
            subprocess.call(['../tdo.py', 'update'])

            fail = False

            try:
                subprocess.call(['tdo'])
            except Exception as err:
                fail = True

            self.assertIs(fail, False, msg='The updater is broken!')
