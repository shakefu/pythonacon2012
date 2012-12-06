from pytool.cmd import Command


class MyCmd(Command):
    def set_opts(self):
        self.opt("--verbose", '-v',
                action='store_true')

    def run(self):
        print "Hello world."
        if self.args.verbose:
            print "Pytool is useful!"

