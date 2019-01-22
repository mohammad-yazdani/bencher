import subprocess
import os


class Runner:

    def __init__(self, executable):
        self.executable = executable

        if os.path.exists(executable + ".in"):
            input_file = open(self.executable + "/" + executable + ".in", "r")
            self.in_str = input_file.read()
            input_file.close()
        else:
            self.in_str = None

    def run_exec(self):
        test_local = "./" + self.executable
        exe = subprocess.run([test_local], input=self.in_str, stdout=subprocess.PIPE)
        return exe
