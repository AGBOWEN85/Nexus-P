import os
import requests
import json
import base64

# Get GitHub token from environment variables
github_token = os.getenv('GITHUB_TOKEN')
if not github_token:
    raise ValueError("GITHUB_TOKEN is not set in the environment!")

headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json"
}

def create_github_repo(repo_name, description="Nexus-P project repository", private=False):
    url = "https://api.github.com/user/repos"
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully!")
        return response.json()['full_name']
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def create_file(repo_full_name, file_path, content, commit_message="Add file"):
    url = f"https://api.github.com/repos/{repo_full_name}/contents/{file_path}"
    data = {
        "message": commit_message,
        "content": base64.b64encode(content.encode()).decode()
    }

    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"File '{file_path}' created successfully!")
    else:
        print(f"Error creating file '{file_path}': {response.status_code} - {response.text}")

def create_folder_structure(repo_full_name):
    folders = [
        "src",
        "tests",
        "docs/api",
        "docs/examples"
    ]

    for folder in folders:
        create_file(repo_full_name, f"{folder}/.gitkeep", "", f"Create {folder} directory")

def create_issue(repo_full_name, title, body):
    url = f"https://api.github.com/repos/{repo_full_name}/issues"
    data = {
        "title": title,
        "body": body
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Issue '{title}' created successfully!")
    else:
        print(f"Error creating issue: {response.status_code} - {response.text}")

def create_initial_issues(repo_full_name):
    issues = [
        {
            "title": "Set up project structure",
            "body": "Create the initial project structure including src/, tests/, and docs/ directories."
        },
        {
            "title": "Implement core functionality",
            "body": "Develop the core functionality of the Nexus-P project."
        },
        {
            "title": "Write unit tests",
            "body": "Create comprehensive unit tests for the core functionality."
        },
        {
            "title": "Document API",
            "body": "Write detailed API documentation for the Nexus-P project."
        }
    ]

    for issue in issues:
        create_issue(repo_full_name, issue["title"], issue["body"])

def create_placeholder_script(repo_full_name):
    content = """
# Nexus-P Core Functionality

class NexusP:
    def __init__(self):
        self.data = {}

    def process(self, input_data):
        # TODO: Implement core processing logic
        pass

    def analyze(self):
        # TODO: Implement data analysis
        pass

    def generate_report(self):
        # TODO: Implement report generation
        pass

if __name__ == "__main__":
    nexus = NexusP()
    # TODO: Add example usage
    print("Nexus-P initialized and ready for use!")
"""
    create_file(repo_full_name, "src/nexus_p.py", content, "Add placeholder Nexus-P script")

def main():
    repo_name = "Nexus-P"
    repo_full_name = create_github_repo(repo_name)
    
    if repo_full_name:
        create_folder_structure(repo_full_name)
        
        # Add README.md
        with open("README.md", "r") as f:
            readme_content = f.read()
        create_file(repo_full_name, "README.md", readme_content, "Add README.md")
        
        # Add .gitignore
        with open(".gitignore", "r") as f:
            gitignore_content = f.read()
        create_file(repo_full_name, ".gitignore", gitignore_content, "Add .gitignore")
        
        # Create initial issues
        create_initial_issues(repo_full_name)
        
        # Create placeholder Python script
        create_placeholder_script(repo_full_name)
        
        print(f"Nexus-P project setup complete. Repository: https://github.com/{repo_full_name}")
    else:
        print("Failed to create the repository. Please check your GitHub token and try again.")

if __name__ == "__main__":
    main()