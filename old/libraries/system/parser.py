# import configparser
# import os
# import system
#
#
# class Parser(object):
#
#     def __init__(self, *where_parse):
#         self.parse_path = os.path.join(*where_parse)
#
#         self.parser = configparser.ConfigParser()
#         self.parser.read(os.path.join(self.parse_path), "UTF-8")
#
#     def sections(self):
#         return self.parser.sections()
#
#     def get(self, section, option):
#         return self.parser.get(section, option).encode().decode(system.System.encoding(), 'ignore')
#
#     def get_list(self, section, option):
#         return self.parser.get(section, option).split("|:|")
#
#     def get_new_line(self, section, option):
#         return self.parser.get(section, option).replace("|:|", "\n")
#
#     def set(self, section, option, result):
#         self.parser.set(section, option, result)
#         with open(self.parse_path, "w", encoding="utf-8") as config_file:
#             self.parser.write(config_file)
