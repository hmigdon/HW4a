import nose
import requests
import json

# Standard library imports...
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_not_none



def number_commits(gitID):
    repos = getRepositories(gitID)
    dict = {}
    for repo in repos:
        repoName = repo["name"]
        dict[repoName] = Commits(gitID, repoName)

    return dict


def getRepositories(gitID):
    URL = "https://api.github.com/users/" + gitID + "/repos"
    r = requests.get(url=URL)
    data = r.json()
    return data


def Commits(gitID, repoName):
    URL = "https://api.github.com/repos/" + gitID + "/" + repoName + "/commits"
    r = requests.get(url=URL)
    data = r.json()
    return len(data)



@patch('project.services.requests.get')
def testing_with_mocks(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = getRepositories('hmigdon')

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)


