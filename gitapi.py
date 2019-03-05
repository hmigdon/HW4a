import requests
import json


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


class Testing(object):
    def test_number_commits(self):
        assert len(number_commits("hmigdon")) > 0

    def test_Repos(self):
        assert len(getRepositories("hmigdon")) > 0

    def test_Commits(self):
        assert Commits('hmigdon', 'triangle2HW') > 0

