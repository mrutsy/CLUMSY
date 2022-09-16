import argparse
import os
import sys
import system
import project


class Api(object):

    def __init__(self):
        self.args = None
        self.arg_parser = None

    def initialization(self):
        self.arg_parser = argparse.ArgumentParser()

        self.arg_parser.add_argument('-np', '--new_project', default=None, help=system.Language().word("help_new_project").get())
        self.arg_parser.add_argument('-rp', '--remove_project', default=None, help=system.Language().word("help_remove_project").get())
        self.arg_parser.add_argument('-frp', '--full_remove_project', default=None, help=system.Language().word("help_full_remove_project").get())
        self.arg_parser.add_argument('-up', '--up_project', default=None, help="Пошел на хуй")
        self.arg_parser.add_argument('-dp', '--down_project', default=None, help="Пошел на хуй")
        self.arg_parser.add_argument('-ns', '--new_site', default=None, help="Пошел на хуй")
        self.arg_parser.add_argument('-ds', '--delete_site', default=None, help="Пошел на хуй")
        self.arg_parser.add_argument("-v", "--version", help="Мудила с нижнего тагила",
                                     action="store_true", default=None)

        self.args = self.arg_parser.parse_args(sys.argv[1:])
        return self

    def handler(self):
        os.system("python3 lib/client.py")
        print(self.args)
        # if self.args.new_project:
        #     project.Project().new(str(self.args.new_project), "")
        # elif self.args.up_project:
        #     print("Поднимаю проект")
        # elif self.args.remove_project:
        #     print("Поднимаю проект")
        # elif self.args.down_project:
        #     print("Закрываю проект")
        # elif self.args.version:
        #     print(system.Settings().version())
        # else:
        #     os.system("python3 lib/client.py")
