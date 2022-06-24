import base64

import pandas as pd


def print_repo(repo):
    # repository full name
    print("Full name:", repo.full_name)
    # repository description
    print("Description:", repo.description)
    # the date of when the repo was created
    print("Date created:", repo.created_at)
    # the date of the last git push
    print("Date of last push:", repo.pushed_at)
    # home website (if available)
    print("Home Page:", repo.homepage)
    # programming language
    print("Language:", repo.language)
    # number of forks
    print("Number of forks:", repo.forks)
    # number of stars
    print("Number of stars:", repo.stargazers_count)
    print("-"*50)
    # repository content (files & directories)
    print("Contents:")
    for content in repo.get_contents(""):
        print(content)
    try:
        # repo license
        print("License:", base64.b64decode(repo.get_license().content.encode()).decode())
    except:
        pass

def repo_dataframe(repo):
    repo_details = {
        "Repo":[repo.full_name],
        "private": [repo.private],
        "archived": [repo.archived],
        "Description":[repo.description],
        "language": [repo.language],
        "Date created":  [repo.created_at],
        "Date of last push:": [repo.pushed_at],
        "open_issues": [repo.open_issues],
        "size KB": [repo.size],
        "default_branch": [repo.default_branch],
        "svn_url": [repo.svn_url],
    }
    df = pd.DataFrame.from_dict(repo_details)
    return df