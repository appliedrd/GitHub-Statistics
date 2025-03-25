from github import Github
import settings

# Authenticate to GitHub
g = Github(settings.access_token)

# Get the authenticated user
user = g.get_user()

# Get the list of repositories
repos = user.get_repos()

# Print the list of repositories
for repo in repos:
    if repo.private:
        print(repo.name)