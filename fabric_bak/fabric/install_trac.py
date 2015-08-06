# -*- coding:utf8 -*-

from fabric.api import local, env

env.shell= "/bin/sh -c"

#主机的密码
env.password= "pabb"

def install():
    """The main method
    """
    local('sudo apt-get install -y trac')
    local('sudo aptitude -y install trac-git')

    #local('sudo apt-get install -y postgresql')
    #local('sudo apt-get install -y python-psycopg2')

    # mysql server has installed
    local('sudo apt-get install -y python-mysqldb')

    local('sudo apt-get install -y libapache2-svn')
    local('sudo apt-get install -y apache2-utils')

    local('sudo apt-get install -y libapache2-mod-python')
    local('sudo a2enmod python')

    # Create group and uses
    local('sudo groupadd subversion')
    local('sudo usermod -G subversion -a pabb')
    local('sudo usermod -G subversion -a www-data')


#$ mysql -uroot  -ppabb --default-character-set=utf8 -e 'GRANT ALL PRIVILEGES ON *.* TO pabb@"%" IDENTIFIED BY "pabb"'
#$ mysql -uroot  -ppabb --default-character-set=utf8 -e 'GRANT ALL PRIVILEGES ON *.* TO pabb@"localhost" IDENTIFIED BY "pabb"'
#$ mysql -uroot -ppabb --default-character-set=utf8 -e 'flush privileges';
##建立数据库 trac
#$ mysql -upabb -ppabb -e 'create database trac default charset utf8 collate utf8_general_ci'



def usage():
    print 'fab -f [file_name] [method_name]'
    print 'eg. fab -f install.py byobu'

if __name__ == '__main__':
    print 'come into main'
