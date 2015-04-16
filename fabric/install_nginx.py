# -*- coding:utf8 -*-

from fabric.api import local, env

env.shell= "/bin/sh -c"

#主机的密码
env.password= "pabb"

def install():
    """The main method
    """
    # old version
    #local("sudo apt-get install -y nginx ")

    #local("sudo apt-get install -y nginx ")
    

    # source
    local('sudo apt-get install -y libpcre3 libpcre3-dev')
    local('sudo apt-get install -y openssl libssl-dev')

    local('wget http://124.205.69.165/files/8000000000027278/nginx.org/download/nginx-1.6.2.tar.gz')
    local('tar -zvxf nginx-1.6.2.tar.gz')
    # do it mannual
    #local('cd nginx-1.6.2/')
    #local('./configure')
    #local('make')
    #local('sudo make install')

    # does not work in fab
    #local('./configure')
    #local('make')
    #local('sudo make install')

    local('cd nginx-1.6.2/ ; ./configure')
    local('cd nginx-1.6.2/ ; make')
    local('cd nginx-1.6.2/ ; sudo make install')


def usage():
    print 'fab -f [file_name] [method_name]'
    print 'eg. fab -f install.py byobu'

if __name__ == '__main__':
    print 'come into main'
