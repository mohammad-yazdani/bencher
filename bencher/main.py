import os
import sys

from bencher.adder import Adder
from bencher.parser import Parser
from bencher.make import Make
from bencher.test import Test

from bencher.ui import UI

TEST_DIR = "tests"
TEST_FILE = "tests/tests.txt"

BUILD_DIR = "build"


def setup():
    if not os.path.exists(TEST_DIR):
        os.mkdir(TEST_DIR)
    if os.path.exists(TEST_FILE):
        test_file = open(TEST_FILE, "r")
    else:
        test_file = open(TEST_FILE, "w+")
    tests_arr = test_file.read().split('\n')
    test_file.close()
    return tests_arr


def run():
    test_lines = setup()
    if "" in test_lines:
        test_lines.remove("")

        # Parse test file
    tests = Parser.parse_tests(test_lines)
    argc = len(sys.argv)
    if argc > 1:
        command = sys.argv[1]
        if command == "add":
            if argc < 3:
                UI.red("ADD: NAME OF TEST REQUIRED!")
            else:
                adder = Adder(TEST_FILE, tests)
                test = sys.argv[2]
                against = None
                if argc is 4:
                    against = sys.argv[3]
                adder.add(test, against)
            exit(0)
        elif command == "list":
            if len(tests) < 1:
                UI.red("NO TESTS IN THE BENCH!")
                exit(1)
            UI.red(UI.breaker("TESTS"))
            for test in tests:
                print("- " + str(test))
            exit(0)

    UI.red(UI.breaker("TEST BENCH"))
    make = Make('make')
    for test in tests:
        make.make_test(test[0])
        against = None
        if len(test) > 1:
            against = test[1]
        test_obj = Test(test[0], comp=against)
        test_obj.run()
        UI.newline()
    make.clean_up()


if __name__ == '__main__':
    run()
