from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import OAuthInteractive

ADD_TENANT_ID = '48d5043c-cf70-4c49-881c-c638f5796997'
ADD_CLIENT_ID = '1b90ede3-271e-401b-81a0-a4d52bea3273' #Azure regiserd app ip
project = 'publicdata'
CDF_CLUSTER = 'api'

creds = OAuthInteractive(
    authority_url=f"https://login.microsoftonline.com/{ADD_TENANT_ID}",
    client_id=ADD_CLIENT_ID,
    scopes=[f"https://{CDF_CLUSTER}.cognitedata.com/.default"],
)

cnf = ClientConfig(
    client_name="Stig",
    project=project,
    credentials=creds,
    base_url=f"https://{CDF_CLUSTER}.cognitedata.com"
)
client = CogniteClient(cnf)