# Copy all user projects from GitLab
This script copies all files for all projects of user on GitLab instance.
1. Get access token from GitLab  
- Go to GitLab -> User settings -> Access tokens.  
- Give name and expiration date, check "read_api" option and press "Create personal access token".
- Copy given key to clipboard and save somewhere
2. Create ssh key and add it to your GitLab account
3. Add to file ~/.ssh/config something like this:  
```
Host gitlabHost
    User    username
    HostName    hostnameOrAddress
    Port    22
    IdentityFile    path/to/created/ssh/key
```
4. Run script in this way  
```python3 main.py <your_api_key> <GitLab_url>```
- GitLab URL may look like: https://my.git.lab.url - **Do not add slash at the end of URL**
