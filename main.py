# Copy all files for projects from GitLab

import requests
import subprocess, shlex
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("apiKey", help = 'GitLab key with "read API" scope. (Go to GitLab -> User settings -> Access tokens. Give name and expiration date, check "read_api" option and press "Create personal access token"')
parser.add_argument("gitlabUrl", help = 'URL to GitLab, e.g. https://my.git.lab.url')

args = parser.parse_args()

gitlabUrl = args.gitlabUrl # URL to GitLab 
key = args.apiKey # GitLab key with "read API" scope
projectsPerPage = 10
baseUrl = '{}/api/v4/projects?simple=true&per_page={}&private_token={}'
url = baseUrl.format(gitlabUrl, projectsPerPage, key)

baseDir = os.getcwd()

while True:
  print('Getting repos from %s ...' % (url))
  response = requests.get(url, verify = False)
  projects = response.json()

  for project in projects:
    project_name = project['name']
    project_path = project['namespace']['full_path']
    project_url = project['ssh_url_to_repo']
    os.chdir(baseDir)

    print('\nProcessing %s...' % project_name)
    try:
      print('\nMoving into %s' % project_path)
      os.makedirs(project_path, exist_ok = True)
      os.chdir(project_path)
      cmd = shlex.split('git clone %s' % project_url)
      subprocess.run(cmd)
    except Exception as e:
      print('Error', e.strerror)

  if 'next' not in response.links:
    break

  url = response.links['next']['url']

print('\nDone')



