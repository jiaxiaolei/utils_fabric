# -*- coding:utf8 -*-

from fabric.api import local, env

env.shell= "/bin/sh -c"

#主机的密码
env.password= "pabb"

def basic():
    print '----basic install'
    # bpython
    local('sudo apt-get -y install bpython')
    ## htop
    #local('sudo apt-get install htop')
    ## make
    #local('sudo apt-get install make')

def byobu():
    #$ sudo apt-get install make
    print '----byobu'
    #local('wget http://launchpad.net/byobu/trunk/3.10/+download/byobu_3.10.orig.tar.gz')
    #local('tar -zvxf byobu_3.10.orig.tar.gz')
    ###print("Executing on %s as %s" % (env.host, env.user))
    #local('cd byobu-3.10/; ./configure')
    local('cd byobu-3.10/; sudo make')
    local('cd byobu-3.10/; sudo make install')

def apache():
    print '----apache'
    local('sudo apt-get install apache2')

def usage():
    print 'fab -f [file_name] [method_name]'
    print 'eg. fab -f install.py byobu'

if __name__ == '__main__':
    print 'come into main'
