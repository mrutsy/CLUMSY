# from dc import docker, dockerCompose
#
# if docker.current_version() is None:
#     docker.install()
# if dockerCompose.current_version() is None:
#     dockerCompose.install()
#
# docker.remove()


import distro
print(distro.id())
print(distro.os_release_info())
print(distro.info())
print(distro.main())
print(distro.distro_release_info())
