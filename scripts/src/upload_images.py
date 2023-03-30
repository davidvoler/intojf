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
    for repo in REPO_LIST:
        image = f"{REGISTRY}/{repo}"
        docker.images.pull(image, tag="latest")
        docker.images.tag(image, tag=release)
        docker.images.push(image, tag=release)
