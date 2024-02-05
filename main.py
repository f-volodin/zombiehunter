import subprocess
import time

def read_server_list():

    with open('server_list.ini') as file:
        content = file.read().splitlines()
    file.close()
    content = content[1:]
    return content

def run_playbook():

    command = "ansible-playbook -i server_list.ini playbook.yml"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
    my_list = result.stdout.splitlines() # I have list with each line of ansible output as string
    servers = read_server_list()

    for server in servers:
        for string in my_list: # I am sorry for this = )
            if server and 'changed=2' in string:
                with open('cleaning_diary.txt', 'a') as file:
                    file.write(f'Server {server} was cleaned on {time.ctime()}\n')
            else:
                pass
    return None

run_playbook()
