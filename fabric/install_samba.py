# -*- coding:utf8 -*-

from fabric.api import local, env

env.shell= "/bin/sh -c"

#主机的密码
env.password= "pabb"

def install():
    """The main method
    """
    ## old version
    #local('sudo apt-get install -y samba')

    ## create sahre
    #local('sudo mkdir -p ~/share')
    #local('sudo chmod 777 ~/share')

    local('sudo smbpasswd pabb')

def usage():
    print 'fab -f [file_name] [method_name]'
    print 'eg. fab -f install.py byobu'

if __name__ == '__main__':
    print 'come into main'
