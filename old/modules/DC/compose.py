import subprocess


def current_version():
    output = str(subprocess.check_output("docker-compose -v", shell=True).rstrip()).replace("b'", "").replace(",", "") \
        .split(" ")

    if output[0] == "docker-compose":
        return output[2]
    else:
        return None
