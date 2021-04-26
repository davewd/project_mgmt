__author__ = "David Dawson"
__copyright__ = "Copyright 2021, David Dawson"
__credits__ = ["David Dawson"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Dave Dawson"
__email__ = "davedawson.co@gmail.com"
__status__ = "Production"

import logging
import requests
import http.client
import json
import datetime

GITHUB_URL = "https://api.github.com/"
GITHUB_OWNER = "davewd"
GITHUB_REPO = "project_mgmt"

logger = logging.getLogger(__name__)


def get_credentials(github_owner: str) -> tuple:
    logger.info("getting credentials...")
    try:
        f = open(f"../secrets/{github_owner}.json", "r")
    except Exception as e:
        logger.info(
            f"Are your owner credentials setup in the secrets folder as owner.json ? {e}")

    file_data = f.read()
    data = json.loads(file_data)
    logger.info(data)
    return (data["username"], data["key"])


def create_jira_epic() -> bool:
    logger.info("Creating Jira Epic")
    pass


def create_jira_story() -> bool:
    pass


def create_github_project(owner: str, repo: str, title: str,) -> bool:
    r = requests.post(f"{GITHUB_URL}/repos/{owner}/{repo}/projects",
                      auth=get_credentials(owner),
                      data=json.dumps({
                          "owner": owner,
                          "repo": repo,
                          "name": f"[short]{title}",
                          "mediaType": {
                              "previews": [
                                'inertia'
                              ]
                          }
                      }))
    return r.status_code == http.client.OK


def create_github_milestone(owner: str, repo: str, title: str, due_date: datetime.date) -> bool:
    r = requests.post(f"{GITHUB_URL}repos/{owner}/{repo}/milestones",
                      auth=get_credentials(owner),
                      data=json.dumps({
                          "title": title,
                          "due_on": due_date.isoformat()
                      }))
    return r.status_code == http.client.OK


create_github_project(GITHUB_OWNER, GITHUB_REPO, "test 123")