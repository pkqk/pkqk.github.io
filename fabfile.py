from fabric.api import *

env.use_ssh_config = True

@task(default=True)
@hosts('pkqk')
def update():
  "Push to github and pull to hosting"
  local("git push")
  with cd('www/pkqk.net'):
    run('git pull')
@task
@hosts('pkqk')
def css():
    with cd('www/pkqk.net/style'):
        run('cat basic.css layout.css mobile.css resume.css > composite.css')

