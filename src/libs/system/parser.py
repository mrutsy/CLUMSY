import src.libs.system as system
import configparser


class ParserIni(object):
    pass


class ParserYml(object):
    pass


class Parser(object):

    def __init__(
            self,
            init_file_path,
    ):
        self.file_path = init_file_path

        self.parser_object = configparser.ConfigParser()
        self.parser_object.read(self.file_path)

    def get(self, section, option):
        try:
            result = self.parser_object.get(section, option)
        except Exception as Error:
            print(Error)
            system.Logger(3, "Ошибка", Error)
        else:
            return result

    def get_section(self):
        try:
            result = self.parser_object.sections()
        except Exception as Error:
            print(Error)
            system.Logger(3, "Ошибка", Error)
        else:
            return result

# from src.libs.system.logger import *
# from src.libs.system.infosys import *
# import configparser
# import os.path
#
#
# class Parser(object):
#
#     def __init__(
#             self,
#             *init_config_file,
#             init_config_path_default=os.path.join("configs"),
#     ):
#         self.config_file = init_config_file
#         self.config_path = init_config_path_default
#
#         self.parser = configparser.ConfigParser()
#         self.parser.read(os.path.join(self.config_path, *self.config_file))
#
#     def get(self, section, option):
#         try:
#             # print(self.parser.sections())
#             result = self.parser.get(section, option)
#             # .encode().decode(InfoSys, 'ignore')
#         except Exception as Error:
#             print(Error)
#         else:
#             return result
#
#     def get_list(self, section, option):
#         try:
#             # print(self.parser.sections())
#             result = self.parser.get(section, option).split("|:|")
#             # .encode().decode(InfoSys, 'ignore')
#         except Exception as Error:
#             print(Error)
#         else:
#             return result
#
#     def get_section(self):
#         try:
#             result = self.parser.sections()
#         except Exception as Error:
#             print(Error)
#         else:
#             return result
#
#
# if __name__ == "__main__":
#     pass
# #     print(Parser("languages.ini").get("sys", "logo"))
