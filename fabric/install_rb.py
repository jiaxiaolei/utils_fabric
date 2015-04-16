# -*- coding:utf8 -*-

from fabric.api import local, env

env.shell= "/bin/sh -c"

#主机的密码
env.password= "pabb"

def install():
    """The main method
    """
    #local('sudo apt-get install -y libapache2-mod-python')
    #local('sudo a2enmod python')

    # 安装 wsgi
    local('sudo apt-get install -y libapache2-mod-wsgi')

   
    # install memcached
    #local('sudo apt-get -y install memcached')

    #local('sudo apt-get install -y mysql-server python-mysqldb libmemcache-dev')
    #local('sudo apt-get install -y  python-svn')
    #local('sudo apt-get install -y patch')


    #NOTE: install reviewboard:

    # method 1
    #local('sudo easy_install reviewboard')
    # time out 

    # method 1
    #local('sudo easy_install reviewboard==2.0.12')
    # return :　error: timed out

    # method 3
    #local('wget http://downloads.reviewboard.org/releases/ReviewBoard/2.0/ReviewBoard-2.0.12-py2.7.egg#md5=efb1ac010b84ee54a071bd253329de69')
    
    local('sudo easy_install ReviewBoard-2.0.12-py2.7.egg')
  
    #local('')
    #local('')
    #local('')
    #local('')

def usage():
    print 'fab -f [file_name] [method_name]'
    print 'eg. fab -f install.py byobu'

if __name__ == '__main__':
    print 'come into main'
