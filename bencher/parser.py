class Parser:

    @staticmethod
    def parse_tests(test_lines):
        tests = list()
        for line in test_lines:
            sig = line.split()
            tests.append(sig)
        return tests
