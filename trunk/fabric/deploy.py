#!/usr/bin/env python
# encoding: utf-8

from fabric.api import local,cd,run,env

#env.hosts=['user@ip:port',] #ssh要用到的参数
#env.hosts=['pabb@192.168.1.107:22',
#           'pabb@192.168.1.108:22',
#           'pabb@192.168.1.3:22',
#           ] 
env.host='pabb@192.168.1.3:22'
env.password = 'pabb' # 远程主机的密码
#env.password = 'pwd' 3 远程主机的密码
#env.passwords = ['pwd']  远程主机的密码
#env.passwords = {'pabb@192.168.1.107:22':'pabb',
#                 'pabb@192.168.1.108:22':'pabb',
#                 'pabb@192.168.1.3:22':'pabb'}

def setting_ci():
    local('echo "add and commit settings in local"')

def update_setting_remote():
    print "remote update"
    with cd('/tmp'):   #cd用于进入远程服务器的某个目录
        run('ls -l | wc -l')  #远程操作用run

def basic():
    print "remote update"
    with cd('/home/pabb/software'):   #cd用于进入远程服务器的某个目录
        #run('sudo apt-get install -y bpython')
        # ipython
        #run('sudo apt-get install -y ipython')
        # zip & unzip
        #run('sudo apt-get install -y zip')
        #run('sudo apt-get install -y unzip')
        # mysql
        run('sudo apt-get install -y mysql-server')

def apache():
    print "remote update"
    with cd('/home/pabb/software'):   #cd用于进入远程服务器的某个目录
        #run('sudo apt-get install -y bpython')
        #run('sudo apt-get install -y apache2')
        #TODO：modify the conf
        #run('sudo service apache2 restart')
        run('sudo apt-get install -y libapache2-mod-php5 php5')
        run('sudo apt-get install -y php5-mysql')

def update():
    setting_ci()
    #update_setting_remote()
    basic()
    #apache()
