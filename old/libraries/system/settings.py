# import os
# import parser
#
#
# class Settings(object):
#     def __init__(self,
#                  settings_path_default=os.path.join("configs", "settings.ini"),
#                  ):
#         self.settings_path = settings_path_default
#
#     def setup_status(self):
#         return bool(int(parser.Parser(self.settings_path).get("program", "setup")))
#
#     def setup_set_true(self):
#         return parser.Parser(self.settings_path).set("program", "setup", "1")
#
#     def setup_set_false(self):
#         return parser.Parser(self.settings_path).set("program", "setup", "0")
#
#     def version(self):
#         return parser.Parser(self.settings_path).get("program", "version")
