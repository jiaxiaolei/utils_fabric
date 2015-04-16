# -*- coding:utf8 -*-

from fabric.api import local, env

env.shell= "/bin/sh -c"

#主机的密码
env.password= "pabb"

def install():
    """The main method
    """
    #local('sudo apt-get install -y git')

    #local("git config --global user.name 'jiaxiaolei'")
    #local("git config --global user.email 'xiaolei.jia@dbjtech.com'")
    #local("git config --global color.ui 'always'")
 
    #local("sudo adduser git")
    local("sudo su git")
    local("ls")


def usage():
    print 'fab -f [file_name] [method_name]'
    print 'eg. fab -f install.py byobu'

if __name__ == '__main__':
    print 'come into main'
