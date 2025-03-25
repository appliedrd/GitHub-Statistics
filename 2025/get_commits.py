from github import Github
import csv
from github import Github
import settings
from datetime import datetime
import xlrd
import openpyxl

# Authenticate to GitHub
g = Github(settings.access_token)

# Create a new Excel workbook and select the active worksheet
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Commits"
# Write the header row
ws.append(['Last Modified', 'Message'])

# Get the repository
repo = g.get_repo("appliedrd/BoisFrancERP")
# open_issues = repo.get_issues(state='open')
# for issue in open_issues:
#     print(issue)

# Get all commits since January 1, 2024
commits = repo.get_commits(since=datetime(2024, 1, 1))

# Print commit SHA and date
# for commit in commits:
#     print(f"Commit: {commit.sha}, Date: {commit.commit.author.date}")

# Write commit data to the Excel file
for commit in commits:
    # Parse the string to a datetime object
    date_obj = datetime.strptime(commit.commit.last_modified, '%a, %d %b %Y %H:%M:%S %Z')
    ws.append([date_obj, commit.commit.message])

# Save the workbook to a file
wb.save('D:\\data\\commits2025-2.xlsx')
