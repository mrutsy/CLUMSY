class Client(object):

    @staticmethod
    def run():
        print("CLIENT")


if __name__ == "__main__":
    pass

# import src.libs.system as system
#
#
# def start():
#     # system.Logger(0, "Запуск консольно-клиентской части.", init_log_show_default=False).running()
#     # print(system.Setting().language_current().get())
#     # print(system.Setting().language_default().get())
#     print(system.Language().get_list())
#     print(system.Language().word())
#     # system.Logger(0, "Консольно-клиентская часть запущена.").success()
#
#
# if __name__ == "__main__":
#     start()
