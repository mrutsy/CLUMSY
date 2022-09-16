import leadership
from web import apache
from containerization import docker

leadership.Api().initialization().handler()


apache.Apache().ok()
docker.Docker().ok()
