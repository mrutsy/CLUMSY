import argparse
import sys

from src.libs import system

print(system.fs.create_dir("logs"))


def init_args():
    arg_parser = argparse.ArgumentParser(
        prog="CLUMSY",
        usage=None,
        description="DESC",
        epilog="EPILOG",
        parents=[],
        formatter_class=argparse.HelpFormatter,
        prefix_chars='-',
        fromfile_prefix_chars=None,
        argument_default=None,
        conflict_handler='error',
        add_help=True,
        allow_abbrev=True,
        exit_on_error=True,
    )
    arg_parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s version: 0.0.1 DEV',
        help="V",
    )
    arg_parser.add_argument(
        '-sp',
        '--select_project',
        default=None,
        help="Выбрать проект."
        # help=languages.Language().word("help_new_project").get()
    )
    arg_parser.add_argument(
        '-np',
        '--new_project',
        default=None,
        help="Создать проект.",

        # help=languages.Language().word("help_new_project").get()
    )
    arg_parser.add_argument(
        '-dp',
        '--delete_project',
        action="store_true",
        help="Удалить проект."
        # help=languages.Language().word("help_new_project").get()
    )
    arg_parser.add_argument(
        '-rp',
        '--rename_project',
        default=None,
        help="Удалить проект."
        # help=languages.Language().word("help_new_project").get()
    )
    arg_parser.add_argument(
        '-rcp',
        '--reconfig_project',
        default=None,
        help="Удалить проект."
        # help=languages.Language().word("help_new_project").get()
    )
    arg_parser.add_argument(
        '-ns',
        '--new_site',
        default=None,
        help="Удалить проект."
        # help=languages.Language().word("help_new_project").get()
    )
    arg_parser.add_argument(
        '-ss',
        '--select_site',
        default=None,
        help="Удалить проект."
        # help=languages.Language().word("help_new_project").get()
    )
    arg_parser.add_argument(
        '-ds',
        '--delete_site',
        default=None,
        help="Удалить проект."
        # help=languages.Language().word("help_new_project").get()
    )
    arg_parser.add_argument(
        '-uc',
        '--update_certificate',
        help="Удалить проект.",
        action="store_true",
        # help=languages.Language().word("help_new_project").get()
    )
    return arg_parser.parse_args(sys.argv[1:])


if __name__ == "__main__":
    if init_args().select_project:
        if init_args().select_site:
            print("site")
        elif init_args().new_project:
            print("ok")
        elif init_args().rename_project:
            print("ok")
        elif init_args().config_project:
            print("ok")
        elif init_args().update_certificate:
            print("ok")
        else:
            print("ERROR - SITE NOT SELECT")
    elif init_args().new_project:
        if init_args().select_site:
            print("site")
        elif init_args().new_project:
            print("ok")
        elif init_args().rename_project:
            print("ok")
        elif init_args().config_project:
            print("ok")
        elif init_args().update_certificate:
            print("ok")
        else:
            print("ERROR - SITE NOT SELECT")
    else:
        import client

        client.start()
