# import src.libs.system as system
#
# import os.path
#
#
# # from src.libs.system.logger import *
# # from src.libs.system.parser import *
#
#
# class Language(object):
#
#     def __init__(
#             self,
#             init_language=None,
#             init_language_path=os.path.join("src", "configs", "language.ini"),
#     ):
#         # Путь до файла конфигурации с языками.
#         self.language_path = init_language_path_default
#         self.language_object = system.Parser(self.language_file_path)
#
#         self.language_current = None
#
#
#
#
#
#
#         language_list = system.Parser(self.language_file_path).get_section()
#         check_language_current = system.Setting().language_current().get()
#         check_language_default = system.Setting().language_default().get()
#
#         if init_language_current is None:
#
#             if check_language_current == "":
#                 if check_language_default == "":
#                     exit("Ошибка - не обнаружен язык по умолчанию.")
#                 else:
#                     if check_language_default in language_list:
#                         print("Язык есть в списке")
#                         self.language_current = check_language_default
#                     else:
#                         print("Языка не существует")
#             else:
#                 if check_language_current in language_list:
#                     print("Текущий Язык есть в списке")
#                 else:
#                     print("Текущего Языка не существует")
#         else:
#             pass
#             # self.language_current = init_language_current
#
#
#     @staticmethod
#     def _get_current():
#         try:
#             result = system.Setting().language_current().get()
#         except Exception as Error:
#             print(Error)
#         else:
#             return result
#
#     @staticmethod
#     def get_default():
#         try:
#             result = system.Setting().language_default().get()
#         except Exception as Error:
#             print(Error)
#         else:
#             return result
#
#     def get_list(self):
#         try:
#             result = system.Parser(self.language_file_path).get_section()
#         except Exception as Error:
#             print(Error)
#         else:
#             return result
#
#     def valid_language(self, language_to_check):
#         if language_to_check in self.get_list():
#             return True
#         else:
#             return False
#
#     def current(self, ):
#         if
#
#     def word(self):
#         print(self.language_current)
