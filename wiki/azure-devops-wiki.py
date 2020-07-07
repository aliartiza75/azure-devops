from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

# Fill in with your personal access token and org URL
personal_access_token = 'ADD_PERSONAL_ACCESS_TOKEN_HERE'
organization_url = 'https://dev.azure.com/ENTER_ORGANIZATION_NAME_HERE'

credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Get a client (the "core" client provides access to projects, teams, etc)
core_client = connection.clients.get_core_client()
# To get wiki client for azure devops wiki manipulation

wiki_client = connection.clients.get_wiki_client()
# Get the first page of projects
get_projects_response = core_client.get_projects()

index = 0
id = None

while get_projects_response is not None:
    for project in get_projects_response.value:
        # print(dir(project))
        id = project.id
        print(project.id)
    if get_projects_response.continuation_token is not None and get_projects_response.continuation_token != "":
        # Get the next page of projects
        get_projects_response = core_client.get_projects(continuation_token=get_projects_response.continuation_token)
    else:
        # All projects have been retrieved
        get_projects_response = None

# To get wikis
wikis = wiki_client.get_all_wikis()
# Iterating over wikis
for item in wikis:
    print(item.id)

# To create a wiki in a project
wiki_client.create_wiki({"name": "WIKI_NAME", "ProjectId": "PROJECT_ID"}, project="PROJECT_NAME")

# To insert data in a wiki
wiki_client.create_or_update_page(parameters={"content": "ENTER_CONTENT HERE", "id": 1},
                                  project="PROJECT_ID",
                                  wiki_identifier="WIKI_NAME",
                                  path="/page1",
                                  version=None)

# To get wiki page
wiki_client.get_page(project="ProjectId", wiki_identifier="")


# To delete wiki page
wiki_client.delete_page(project="ProjectId", wiki_identifier="")
