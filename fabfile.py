from fabric.api import *

env.use_ssh_config = True

@task(default=True)
@hosts('pkqk')
def update():
    "Push to github and pull to hosting"
    local("git push")
    with cd('www/pkqk.net'):
        run('git checkout style/composite.css')
        run('git pull')
    css()

@task
@hosts('pkqk')
def css():
    with cd('www/pkqk.net/style'):
        run('cat basic.css layout.css mobile.css resume.css print.css > composite.css')
