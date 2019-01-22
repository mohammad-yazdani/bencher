import os
from bencher.runner import Runner
from bencher.diff import Diff
from bencher.ui import UI


class Test:

    def __init__(self, name, comp=None):
        self.name = name
        self.runner = Runner(executable=name)

        comp_runner = None
        if comp is not None:
            comp_runner = Runner(comp)
        self.diff = Diff(name, comp_runner)

    def run(self):
        UI.yellow("> " + self.name)

        res = self.runner.run_exec()
        if res.returncode is not 0:
            UI.red("TEST CRASHED [code " + str(res.returncode) + "]: " + self.name)
            UI.red(res.stdout.decode())
        else:
            UI.yellow("TEST RAN: " + self.name)
            os.remove(self.name + ".act")
            act = open(self.name + ".act", "w")
            act.write(res.stdout.decode())
            act.close()

        err, out = self.diff.compare_output()
        if err is 0:
            UI.green("TEST PASSED: " + self.name)
        else:
            UI.red("TEST FAILED [code " + str(err) + "]: " + self.name)
            UI.red(out)
