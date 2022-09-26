import sys
from libs import container

print(sys.argv)

container.docker.print_test()
container.docker_compose.print_test()
