# -*- coding:utf8 -*-

# 导入Fabric API:
from fabric.api import *

# # 服务器登录用户名:
# env.user = 'cic'
# # sudo用户为root:
# env.sudo_user = 'cic'
# env.password='Hkhl2015'


##

# 服务器登录用户名:
env.user = 'w_jiaxiaolei'
# sudo用户为root:
env.sudo_user = 'w_jiaxiaolei'
env.password='111111'




# 服务器地址，可以有多个，依次部署:
# env.hosts = ['127.0.0.1']

env.hosts=['101.200.189.202']


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



def usage():
    print('fab -f 1.py hello')
 

if __name__ == '__main__':
    print 'xxxx'
