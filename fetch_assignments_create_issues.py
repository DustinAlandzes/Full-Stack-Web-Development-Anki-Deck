import logging
import random

from github import Github

from bootcampspot import BootcampSpot
from settings import ACCESS_TOKEN, REPOSITORY, ASSIGNEE_CHOICES


def create_issues_for_assignments():
    g = Github(ACCESS_TOKEN)
    repo = g.get_repo(REPOSITORY)
    open_issues = list(repo.get_issues(state='open'))
    closed_issues = list(repo.get_issues(state='closed'))
    open_issue_titles = [issue.title for issue in open_issues]
    existing_issues = open_issue_titles.copy()
    existing_issues.extend([issue.title for issue in closed_issues])
    logging.info(f"Fetched existing issues from Github.")

    bootcamp_spot = BootcampSpot()
    assignments = bootcamp_spot.get_assignments()
    logging.info(f"Fetched assignments from Bootcamp Spot.")
    for assignment in assignments:
        title = f"{assignment.get('studentName')} - {assignment.get('assignmentTitle')}"
        added_already = title in existing_issues
        is_submitted = assignment.get('submitted')
        graded = assignment.get('grade')
        not_a_milestone = 'Milestone' not in assignment.get('assignmentTitle')
        is_an_open_issue = title in open_issue_titles

        if added_already and graded and is_an_open_issue:
            issue_number = open_issues[open_issue_titles.index(title)].number
            repo.get_issue(issue_number).edit(state='closed')

        if all([not added_already, is_submitted, not graded, not_a_milestone]):
            assignee_choice = random.choice(ASSIGNEE_CHOICES)
            repo.create_issue(title=title, assignee=assignee_choice)
            existing_issues.append(title)
            logging.info(f"Assigned {title} to {assignee_choice}.")
    return existing_issues


if __name__ == "__main__":
    create_issues_for_assignments()
