from fabric.api import local, env, settings, abort, run, cd

env.shell="/bin/sh -c"
env.user='pabb'
env.host=['localhost']

def byobu():
    #local('wget http://launchpad.net/byobu/trunk/3.10/+download/byobu_3.10.orig.tar.gz')
    #local('tar -zvxf byobu_3.10.orig.tar.gz')
    print("Executing on %s as %s" % (env.host, env.user))
    with cd('byobu-3.10'):
        run('ls')
#    #local('/bin/bash configure')
#    local('/bin/bash byobu-3.10/configure')
#    local('sudo make')
#    local('sudo make install')
#
