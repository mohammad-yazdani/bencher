import subprocess

from bencher.ui import UI


class Diff:

    def __init__(self, name, test_dir, runner=None):
        act_file = open(test_dir + "/" + name + ".act", "r")
        self.actual = act_file.read()
        act_file.close()
        if runner is None:
            exp_file = open(test_dir + "/" + name + ".exp", "r")
            self.expected = exp_file.read()
            exp_file.close()
        else:
            res = runner.run_exec()
            if res.returncode is not 0:
                UI.red(res.stdout)
                UI.red(res.stderr)
                raise Exception(res.stderr)
            else:
                self.expected = res.stdout.decode()

    def compare_output(self):
        res = subprocess.run(['diff', self.actual, self.expected], stdout=subprocess.PIPE)
        if len(res.stdout.decode()) is 0:
            return 0, None
        else:
            return 1, res.stdout.decode()
