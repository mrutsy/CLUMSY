import system


class Interface(object):

    @staticmethod
    def view(lang, what):
        for line in system.Parser().init("configs", "languages.ini").get(lang, what, True):
            print(line)
        print("\n")
