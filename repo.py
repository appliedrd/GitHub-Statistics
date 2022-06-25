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
    # programming language
    print("Language:", repo.language)
    # number of forks
    print("Number of forks:", repo.forks)
    # number of stars
    print("Number of stars:", repo.stargazers_count)
    print("-" * 50)
    # repository content (files & directories)
    print("Contents:")
    for content in repo.get_contents(""):
        print(content)
    try:
        # repo license
        print("License:", base64.b64decode(repo.get_license().content.encode()).decode())
    except:
        pass


def repo_dataframe(g, repo):
    repo_details = {
        "Repo": [repo.full_name],
        "private": [repo.private],
        "archived": [repo.archived],
        "Description": [repo.description],
        "language": [repo.language],
        "Date created": [repo.created_at],
        "Date of last push:": [repo.pushed_at],
        "open_issues": [repo.open_issues],
        "size KB": [repo.size],
        "default_branch": [repo.default_branch],
        "svn_url": [repo.svn_url],
    }

    collab_list = ""
    repo_collaborators = g.get_repo(repo.full_name)
    collaborators = repo_collaborators.get_collaborators()
    for collaborator in collaborators:
        collab_list = collab_list + " | " + collaborator.login
    repo_details["collaborators"] = collab_list

    try:
        pending_invitations = g.get_repo(repo.full_name).get_pending_invitations()
        repo_details["pending_invitations"] = pending_invitations.totalCount
    except:
        repo_details["pending_invitations"] = -1

    df = pd.DataFrame.from_dict(repo_details)
    return df


# def get_repo_invitations(g, repo):
#     pi = g.get_repo(repo.full_name).get_pending_invitations()
#     if pi.totalCount > 0:
#         print(pi)
#     return pi
