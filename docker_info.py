import docker


class Docker_collecter:
    def __init__(self):
        self.client = docker.from_env()

    def get_container_count(self):
        try:
            containers = len(self.client.containers.list())
        except Exception:
            containers = 0
        return containers
