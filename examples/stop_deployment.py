from vendi import Vendi

client = Vendi(
    api_key="my-api-key"
)

deployments = client.deployments.list()

for deployment in deployments:
    if deployment.name == "mistral-7b-sdk":
        client.deployments.stop(
            deployment_id=deployment.id
        )
        print("Deployment stopped")
