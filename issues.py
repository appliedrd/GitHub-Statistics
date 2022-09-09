from github import Github
import pandas as pd
import settings

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Github username
from issue import issue_dataframe

issueList = []
first = True
g = Github(settings.access_token)
repo = g.get_repo("mauspaiva/physiobiometrics")
open_issues = repo.get_issues(state='open')
for issue in open_issues:
    print(issue)
    df = issue_dataframe(g, issue)
    if first:
        issueList = df
        first = False
    else:
        issueList = issueList.append(df)
issueList.to_csv(settings.output_issues)