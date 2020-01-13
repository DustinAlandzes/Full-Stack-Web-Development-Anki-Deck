import os
import random

from github import Github

from bootcampspot import BootcampSpot

REPOSITORY = os.environ.get('REPOSITORY')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ASSIGNEE_CHOICES = os.environ.get('ASSIGNEE_CHOICES', '').split(',')


def create_issues_for_assignments():
    g = Github(ACCESS_TOKEN)
    repo = g.get_repo(REPOSITORY)
    open_issues = list(repo.get_issues(state='open'))
    closed_issues = list(repo.get_issues(state='closed'))
    existing_issues = [issue.title for issue in open_issues]
    existing_issues.extend([issue.title for issue in closed_issues])

    bootcamp_spot = BootcampSpot()
    assignments = bootcamp_spot.get_assignments()
    for assignment in assignments:
        title = f"{assignment.get('studentName')} - {assignment.get('assignmentTitle')}"

        not_added_already = title not in existing_issues
        is_submitted = assignment.get('submitted')
        not_graded = not assignment.get('grade')
        not_a_milestone = 'Milestone' not in assignment.get('assignmentTitle')
        if all([not_added_already, is_submitted, not_graded, not_a_milestone]):
            repo.create_issue(title=title, assignee=random.choice(ASSIGNEE_CHOICES))
            existing_issues.append(title)
    return existing_issues


if __name__ == "__main__":
    create_issues_for_assignments()
