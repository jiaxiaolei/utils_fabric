from fabric.api import local, env

env.shell= "/bin/sh -c"

def byobu():
    #local('wget http://launchpad.net/byobu/trunk/3.10/+download/byobu_3.10.orig.tar.gz')
    #local('tar -zvxf byobu_3.10.orig.tar.gz')
    print("Executing on %s as %s" % (env.host, env.user))
    #local('cd ~/software/byobu-3.10/')
    local('ls')
    #local('/bin/bash configure')
    local('/bin/bash byobu-3.10/configure')
    local('sudo make')
    local('sudo make install')

