from dc import docker, dockerCompose

if docker.current_version() is None:
    docker.install()
if dockerCompose.current_version() is None:
    print("DockerCompose is None")


