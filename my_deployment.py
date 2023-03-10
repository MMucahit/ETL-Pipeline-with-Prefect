from Transform import main
from prefect.deployments import Deployment

from prefect.filesystems import LocalFileSystem
from prefect.filesystems import LocalFileSystem

local_file_system_block = LocalFileSystem.load("titanic-storage-block")

local_file_system_block = LocalFileSystem.load("titanic-storage-block")

deployment = Deployment.build_from_flow(
    flow=main,
    name="titanic-deployment"
)

if __name__ == "__main__":
    deployment.apply()