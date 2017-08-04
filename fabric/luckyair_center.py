# -*- coding:utf8 -*-

# 导入Fabric API:
from fabric.api import *

# # 服务器登录用户名:
# env.user = 'cic'
# # sudo用户为root:
# env.sudo_user = 'cic'
# env.password='Hkhl2015'


# # 服务器登录用户名:
# env.user = 'cic'
# # sudo用户为root:
# env.sudo_user = 'cic'
# env.password='Hkhl2015'


# # 服务器地址，可以有多个，依次部署:
# # env.hosts = ['127.0.0.1']

# # env.hosts=['101.200.189.202']
# env.hosts=['101.200.199.125']

env.host='cic@101.200.199.125:22'
env.password='Hkhl2015'


def hello():
    print("Hello world!")
    local('pwd')
    #run('pwd')


    #with cd('/tmp'):   #cd用于进入远程服务器的某个目录
    #    # run('ls -l | wc -l')  #远程操作用run

    #    print('-----cd')
    #    run('pwd')
    #    run('ls -l')

    ## with lcd(path) 返回的还是 /home/user 目录， 没生效？？ 
    with lcd('/tmp'):   #cd用于进入远程服务器的某个目录
        print('----lcd')
        run('pwd')
        # run('ls -l | wc -l')  #远程操作用run
        run('ls -l')

def sync_log():

    run("rsync -arv /var/log/supervisor cic@101.200.199.125:/home/cic/log_keep/luckyair_test_204")
    # run("sshpass rsync -arv /var/log/supervisor cic@101.200.199.125:/home/cic/log_keep/luckyair_test_204")



def usage():
    print('fab -f 1.py hello')
 

if __name__ == '__main__':
    print 'xxxx'
