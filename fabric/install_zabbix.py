# -*- coding:utf8 -*-

from fabric.api import local, env

env.shell= "/bin/sh -c"

#主机的密码
env.password= "pabb"

def install():
    """The main method
    """
    
    # create group and user
    #local('sudo groupadd zabbix')
    #local('sudo useradd zabbix -g zabbix')
    local('sudo usermod -G zabbix -a pabb')

    #local('')
    #local('')
    #local('')

def usage():
    print 'fab -f [file_name] [method_name]'
    print 'eg. fab -f install.py byobu'

if __name__ == '__main__':
    print 'come into main'
