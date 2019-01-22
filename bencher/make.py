import subprocess
import os

from bencher.ui import UI

# Temporary: only works with make


class Make:

    def __init__(self, agent, args=None):
        self.agent = agent
        self.args = args

        if agent is 'make':
            if not os.path.exists('Makefile'):
                UI.red("No Makefile found!")
                exit(1)

    def make_test(self, test):
        UI.purple("BUILDING:")
        make = subprocess.run([self.agent, test], stdout=subprocess.PIPE)
        if make.returncode != 0:
            UI.red(str(make.stdout.decode()))
            UI.red("RETURN CODE: " + str(make.returncode))
        else:
            UI.green(str(make.stdout.decode()))

    def clean_up(self):
        make = subprocess.run([self.agent, 'clean'], stdout=subprocess.PIPE)
        if make.returncode != 0:
            UI.red(str(make.stdout.decode()))
            UI.red("RETURN CODE: " + str(make.returncode))
        else:
            UI.green(str(make.stdout.decode()))
