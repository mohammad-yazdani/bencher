RED = "\033[0;31m"
GREEN = "\033[0;32m"
PURPLE = "\033[35m"
YELLOW = "\033[93m"

RESET = "\033[0;0m"
SPLIT = " ========================= "


class UI:

    @staticmethod
    def red(msg):
        print(RED + msg + RESET)

    @staticmethod
    def green(msg):
        print(GREEN + msg + RESET)

    @staticmethod
    def purple(msg):
        print(PURPLE + msg + RESET)

    @staticmethod
    def yellow(msg):
        print(YELLOW + msg + RESET)

    @staticmethod
    def newline():
        print('')

    @staticmethod
    def breaker(msg):
        return SPLIT + msg + SPLIT
