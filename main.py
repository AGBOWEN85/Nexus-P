import os
import requests

# Get the GitHub token from the environment variables
github_token = os.getenv('GITHUB_TOKEN')
if not github_token:
    raise ValueError("GITHUB_TOKEN is not set in the environment!")

GITHUB_USERNAME = 'AGBOWEN85'  # Your GitHub username

def create_github_repo(repo_name):
    """Create a new GitHub repository using the GitHub API."""
    url = f"https://api.github.com/user/repos"
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        "name": repo_name,
        "private": False,  # Set to True if you want the repo to be private
        "description": "Nexus-P project repository",
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"GitHub repository {repo_name} created successfully!")
    else:
        print(f"Error creating GitHub repository: {response.status_code} - {response.text}")

if __name__ == "__main__":
    repo_name = "Nexus-P"  # You can change this name if you want a different repo name
    create_github_repo(repo_name)
