import subprocess
import os


def remove():
    os.system("sudo dnf remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-selinux \
                  docker-engine-selinux \
                  docker-engine -y")


def current_version():
    output = str(subprocess.check_output("docker -v", shell=True).rstrip()).replace("b'", "").replace(",", "") \
        .split(" ")

    if output[0] == "Docker":
        return output[2]
    else:
        return None
