import argparse
import os
import sys
import system
import interface

class Api(object):

    def __init__(self):
        self.args = None
        self.arg_parser = None

    def initialization(self):
        self.arg_parser = argparse.ArgumentParser()
        self.arg_parser.add_argument('-np', '--new_project', default=None, help=system.Language().lang().word("help_new_project").get())
        self.arg_parser.add_argument('-up', '--up_project', default=None, help="Пошел на хуй")
        self.arg_parser.add_argument('-dp', '--down_project', default=None, help="Пошел на хуй")
        self.arg_parser.add_argument('-ns', '--new_site', default=None, help="Пошел на хуй")
        self.arg_parser.add_argument('-ds', '--delete_site', default=None, help="Пошел на хуй")
        # self.arg_parser.add_argument('-h', '--help', action="help", help="ddddd")
        self.arg_parser.add_argument("-v", "--version", help="Мудила с нижнего тагила",
                                     action="store_true")
        self.args = self.arg_parser.parse_args(sys.argv[1:])
        return self

    def handler(self):
        if self.args.new_project:
            system.Files.new_folder(format(self.args.new_project))
            print("{}".format(self.args.new_project))
        elif self.args.up_project:
            print("Поднимаю проект")
        elif self.args.down_project:
            print("Закрываю проект")
        elif self.args.version:
            print("{}".format(self.args.version))
        else:
            os.system("python3 lib/client.py")
