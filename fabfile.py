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
        files = run('ls -1 *.css').split("\r\n")
        files.remove('composite.css')
        run('cat %s > composite.css' % " ".join(files))

