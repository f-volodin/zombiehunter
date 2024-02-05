# ZOMBIEHUNTER

Welcome to my project! This program is running ansible playbook to delete unnecesary *.s3 zombie processes on cloud server which are stored in /tmp folder.

Ansible playbook will check if disk space in /tmp folder is filled more than 85%, and in case it is, it's gonna delete all *.s3 files (a.k.a. zombie processes) if there are any, as this should free some sapce. Python will also write which servers are cleaned and when in cleaning_diary.txt file. 

## Getting Started

Follow these steps to get started:

1. Clone the repository.
2. Install python3 and ansible
3. Add your servers into server_list.ini file
4. Run 'python3 main.py' in terminal
