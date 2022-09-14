import parser


def view(lang, what):
    for line in parser.Parser().init("configs", "language.ini").get(lang, what, True):
        print(line)
    print("\n")
