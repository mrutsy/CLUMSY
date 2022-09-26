import subprocess


def install():
    pass


def current_version():
    output = None
    try:
        output = subprocess.check_output(['docker-compose -v'], shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as Error:
        if Error.args[0] == 127:
            output = None
        elif Error.args[0] == 1:
            output = None
        else:
            print(Error)
    finally:
        if output is None:
            return output
        else:
            return str(output).rstrip().replace("b'", "").replace(",", "").split(" ")[2]
