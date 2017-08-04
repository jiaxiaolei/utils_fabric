#!/usr/bin/python

"""Add public key of master-host to slave hosts.
"""
 
from fabric.colors import red, green
from fabric.context_managers import cd
from fabric.operations import *
from fabric.api import *

#env.roledefs = {
#    'master':['192.168.1.3'],
#    'slave':['192.168.1.107', '192.168.1.108']
#    }


# $ ssh-keygen -t rsa -P "" 

all_host = ['192.168.1.3',
            '192.168.1.5',
            '192.168.1.8',
            #'192.168.1.9',
            '192.168.1.101',
            #'192.168.1.102',
            '192.168.1.103',
            #'192.168.1.104',
            #'192.168.1.105',
            '192.168.1.106',
            '192.168.1.107',
            '192.168.1.108',
            #'192.168.1.109',

            '192.168.1.205',
            '192.168.1.206',
            '192.168.1.207', ]

master_host = ['192.168.1.106']
slave_host = list(set(all_host)-set(master_host))
env.roledefs = {
    'master': master_host,
    'slave': slave_host,
}
env.user= 'pabb'
env.password = 'pabb'
 
def color():
    local('ls -l | wc -l')
    print(red("This sentence is red, except for ", bold=True) \
            + green("these words, which are green."))
 
def ctx_mgr():
    with cd('/var/www'):
        run('ls')
 
@roles('master')
def get_sshkey():
    get('/home/pabb/.ssh/id_rsa.pub', 'id_rsa.pub.master')
 
@roles('slave')
def put_sshkey():
    with cd('/tmp'):
        put('id_rsa.pub.master', 'id_rsa.pub.master')
        run('cat id_rsa.pub.master >> /home/pabb/.ssh/authorized_keys')
 
def do_task():
    execute(get_sshkey)
    execute(put_sshkey)
