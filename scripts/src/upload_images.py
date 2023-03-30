import docker 

REGISTRY = 'artifactory.localhost'

REPO_LIST = [
    "backend_python",
    "backend_java",
    "fontend_angular",
]

def create_release(release: str):
    client = docker.from_env()
    images = docker.images.list()

    for img in images:
        client.images.push('myimage', tag='latest')