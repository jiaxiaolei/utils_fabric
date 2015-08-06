# -*- coding:utf8 -*-

from fabric.api import local, env

env.shell= "/bin/sh -c"

#主机的密码
env.password= "pabb"

def install():
    """The main method
    """
#    local('cd ~; touch test106.txt')

    # check out code
    #local('cd ~; svn co http://pabb-608/svn/lbs ABT')
    #local('cd ~; svn co http://pabb-608/svn/acb acb')
    #local('cd ~; svn co http://pabb-608/svn/clw clw')

    # update


    # copy site
    #local('sudo scp pabb@pabb-608:/etc/nginx/sites-available/* /etc/nginx/sites-available')
    local('sudo scp pabb@pabb-608:/etc/nginx/sites-enabled/* /etc/nginx/sites-enabled')

    # https keys
    #local('sudo scp pabb@pabb-608:/etc/nginx/*.key /etc/nginx/')
    #local('sudo scp pabb@pabb-608:/etc/nginx/*.crt /etc/nginx/')
    #local('sudo scp pabb@pabb-608:/etc/nginx/*.cer /etc/nginx/')
    #local('sudo scp -r pabb@pabb-608:/etc/nginx/qiji_key /etc/nginx/')

    #local('cd ~; touch test106.txt')
    #local('cd ~; touch test106.txt')
    #local('cd ~; touch test106.txt')

def usage():
    print 'fab -f [file_name] [method_name]'
    print 'eg. fab -f install.py byobu'

if __name__ == '__main__':
    print 'come into main'
