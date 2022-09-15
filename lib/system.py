import configparser
import os
import sys


class System(object):
    @staticmethod
    def encoding():
        if sys.platform == "linux" or sys.platform == "linux2":
            return "utf-8"
        elif sys.platform == "darwin":
            pass
        elif sys.platform == "win32":
            return "cp1251"


class Parser(object):

    def __init__(self, *where_parse):
        self.parse_path = os.path.join(*where_parse)

        self.parser = configparser.ConfigParser()
        self.parser.read(os.path.join(self.parse_path), "UTF-8")

    def sections(self):
        return self.parser.sections()

    def get(self, section, option):
        return self.parser.get(section, option).encode().decode(System.encoding(), 'ignore')

    def get_list(self, section, option):
        return self.parser.get(section, option).split("|:|")

    def get_new_line(self, section, option):
        return self.parser.get(section, option).replace("|:|", "\n")

    def set(self, section, option, result):
        self.parser.set(section, option, result)
        with open(self.parse_path, "w", encoding="utf-8") as config_file:
            self.parser.write(config_file)


class Logger(object):
    def __init__(self, error_code, *format_arg):
        print(Language().word(error_code, *format_arg).get())


class Files(object):

    @staticmethod
    def new_folder(*path):

        if os.path.isdir(os.path.join(*path)):
            Logger("error_creating_folder_already_created", os.path.join(*path))
        else:
            os.mkdir(os.path.join(*path))


class Settings(object):
    def __init__(self,
                 settings_path_default=os.path.join("configs", "settings.ini"),
                 ):
        self.settings_path = settings_path_default

    def setup_status(self):
        return bool(int(Parser(self.settings_path).get("program", "setup")))

    def setup_set_true(self):
        return Parser(self.settings_path).set("program", "setup", "1")

    def setup_set_false(self):
        return Parser(self.settings_path).set("program", "setup", "0")

    def version(self):
        return Parser(self.settings_path).get("program", "version")


class Language(object):
    def __init__(self,
                 language_default=Parser(Settings().settings_path).get("program", "language"),
                 language_path_default=os.path.join("configs", "languages.ini")
                 ):
        self.language = language_default
        self.language_path = language_path_default
        self.received_word = None

    def word(self, receive_word, *format_arg):
        if format_arg:
            self.received_word = Parser(self.language_path).get(self.language, receive_word).format(*format_arg)
        else:
            self.received_word = Parser(self.language_path).get(self.language, receive_word)
        return self

    def console(self):
        for line in str(self.received_word).split("|:|"):
            print(line)

    def get(self):
        return self.received_word


#
# Logger(Settings().version())
# Language().word("test", "Роман", "23", "ахуе").show()
# print(Language().word("test", "Роман", "23", "ахуе").get())
#
# print(Parser(Language().language_path).get_new_line("system", "logo"))
# Files().new_folder("configs", "zhilk.in")
