import base64

import pandas as pd



def issue_dataframe(g, issue):
    issue_details = {
        "created": [issue.created_at],
        "milestone": [issue.milestone],
        "title": [issue.title],
        "assignee": [issue.assignee],
        "state": [issue.state],
        "body": [issue.body],
        "labels": [issue.labels],

    }
    df = pd.DataFrame.from_dict(issue_details)
    return df


# def get_repo_invitations(g, repo):
#     pi = g.get_repo(repo.full_name).get_pending_invitations()
#     if pi.totalCount > 0:
#         print(pi)
#     return pi
