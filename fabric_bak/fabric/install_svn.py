# -*- coding:utf8 -*-

from fabric.api import local, env

env.shell= "/bin/sh -c"

#主机的密码
env.password= "pabb"

def install():
    """The main method
    """

    #local('sudo apt-get -y install subversion apache2')
    #local('sudo apt-get -y install libapache2-svn')
    ## 安装 htpasswd 插件
    #local('sudo apt-get install apache2-utils')

    # Create group and uses
    #local('sudo groupadd subversion')
    #local('sudo usermod -G subversion -a pabb')
    #local('sudo usermod -G subversion -a www-data')


def usage():
    print 'fab -f [file_name] [method_name]'
    print 'eg. fab -f install.py byobu'

if __name__ == '__main__':
    print 'come into main'
