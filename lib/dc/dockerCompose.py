import subprocess


def current_version():
    output = None
    try:
        output = subprocess.check_output(['docker-compose -v'], shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as Error:
        if Error.args[0] == 127:
            output = None
        else:
            print(Error)
    finally:
        if output is None:
            return output
        else:
            return str(output).rstrip().replace("b'", "").replace(",", "").split(" ")[2]

    # error = None
    # result = None
    #
    # try:
    #
    #     result = str(subprocess.check_output("docker -v", shell=True)).rstrip()
    # except Exception as error:
    #     if error.args[0] == 127:
    #         print(error.args[0])
    #     else:
    #         return "unknow"
    # finally:
    #     return "eeee"
    # # finally:
    # #     if error is None:
    # #         return result.rstrip().replace("b'", "").replace(",", "").split(" ")[2]
