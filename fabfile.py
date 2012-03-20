from fabric.api import *

env.use_ssh_config = True
env.hosts.append('pkqk')

@task(default=True)
def update():
  "Push to github and pull to hosting"
  local("git push")
  with cd('www/pkqk.net'):
    run('git pull')
