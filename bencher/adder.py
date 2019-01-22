from bencher.ui import UI


class Adder:

    def __init__(self, config_file, tests):
        self.tests = tests
        self.config_file = config_file

    def add(self, new_test, against=None):
        test_file = open(self.config_file, "a")

        suite = [new_test]
        if against is not None:
            suite.append(against)
        else:
            against = ''
        if suite in self.tests:
            UI.red("TEST ALREADY IN THE BENCH!")
        else:
            test_file.write(new_test + " " + against + '\n')
            UI.green("ADDED " + new_test + " " + against)
        test_file.close()
