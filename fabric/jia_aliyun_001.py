#!/usr/bin/env python
# coding=utf-8


"""
fabric 是支持无密码操作rsync 到远程目录的。 
"""
from fabric.api import local,cd,run, env
 
# Template
# env.hosts=['user@ip:port',] #ssh要用到的参数
# env.password = 'pwd'
 
# user and password
# env.hosts=['pabb@101.200.85.155:22',] #ssh要用到的参数
# env.password = 'pabb'


# 使用 ssh 达到无密码登陆的目的。
env.hosts=['101.200.85.155:22',] #ssh要用到的参数
env.key_filename = "~/.ssh/id_rsa"


cmd = ' rsync -arv /var/log/apache2 1.py pabb@www.jiaxiaolei.com:/home/pabb/test'
# cmd = ' rsync -arv  1.py pabb@www.jiaxiaolei.com:/home/pabb/test'
def setting_ci():
    local('echo "add and commit settings in local"')
    local(cmd)


    #刚才的操作换到这里，你懂的
 
def update_setting_remote():
    print "remote update"
    with cd('~/test'):   #cd用于进入某个目录
        run('ls -l ')  #远程操作用run
        run('ls -l | wc -l')  #远程操作用run

        # rsync_cmd = ''
 
def update():
    setting_ci()
    update_setting_remote()

