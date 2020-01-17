import os

'''
boot camp spot
'''
EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')

# you can get this from the /api/instructor/v1/me endpoint
COURSE_ID = int(os.environ.get('COURSE_ID'))

'''
github
'''
REPOSITORY = os.environ.get('REPOSITORY')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')

# this is a list of github usernames separated by commas (,)
ASSIGNEE_CHOICES = os.environ.get('ASSIGNEE_CHOICES', '').split(',')
