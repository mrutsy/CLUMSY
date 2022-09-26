from system import language


def client_start():
    language.Language().test()
    print("@OK")


client_start()

if __name__ == "__main__":
    client_start()
