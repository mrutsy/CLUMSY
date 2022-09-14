import subprocess
import os
import platform
import distro

def remove():

    distro.distro_release_info()
    if platform == "linux" or platform == "linux2":

    elif platform == "darwin":
    elif platform == "win32":

    os.system("sudo dnf remove docker-ce docker-ce-cli containerd.io docker-compose-plugin -y")
    os.system(
        "sudo \
         dnf remove \
                  docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-selinux \
                  docker-engine-selinux \
                  docker-engine \
                  -y"
    )


def install():
    os.system("sudo sh "+os.path.join("lib", "dc", "get_docker.sh"))


def current_version():
    output = None
    try:
        output = subprocess.check_output(['docker -v'], shell=True, stderr=subprocess.STDOUT)
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
