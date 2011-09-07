import fabric
from fabric.api import *
import sys

env.hosts = ['USER@HOSTNAME'] 

def deploy():
    _check_code()
    code_dir = 'WHERE YOU STORE YOUR CODE, e.g. /srv/www/'
    with cd(code_dir):
        run("git pull origin master")
        run('/etc/init.d/apache2 reload')

def _check_code():
    file_list = local("git status --porcelain", capture=True)
    files = file_list.split('\n')
    if files[0] != "":
        print("Unchecked in files...")
        for f in files:
            print(f)
        if fabric.contrib.console.confirm("There are files not checked in. Are you sure you want to continue?"):
            print("Continuing with deployment...")
        else:
            print("Quitting deployment")
            sys.exit()



