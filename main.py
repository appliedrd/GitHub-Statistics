from github import Github
import pandas as pd
import settings

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Github username
from repo import print_repo, repo_dataframe

g = Github(settings.access_token)

# Then play with your Github objects:

# for repo in g.get_user().get_repos():
#     print(repo.name)
#     print_repo(repo)

git_repos = []
first = True
for repo in g.get_user().get_repos():
    if repo.private and not repo.archived:
        df = repo_dataframe(g, repo)
        if first:
            git_repos = df
            first = False
        else:
            git_repos = git_repos.append(df)

git_repos.to_csv(settings.output_csv)

