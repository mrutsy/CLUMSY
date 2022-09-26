from system import logger


class Language(object):
    @staticmethod
    def test():
        print("OK")

# import os
#
# from settings import *
#
#
# class Language(object):
#     def __init__(self,
#                  language_default=parser.Parser(Settings().settings_path).get("program", "language"),
#                  language_path_default=os.path.join("configs", "languages.ini")
#                  ):
#         self.language = language_default
#         self.language_path = language_path_default
#         self.received_word = None
#
#     def word(self, receive_word, *format_arg):
#         if format_arg:
#             self.received_word = parser.Parser(self.language_path).get(self.language, receive_word).format(*format_arg)
#         else:
#             self.received_word = parser.Parser(self.language_path).get(self.language, receive_word)
#         return self
#
#     def console(self):
#         for line in str(self.received_word).split("|:|"):
#             print(line)
#
#     def get(self):
#         return self.received_word
