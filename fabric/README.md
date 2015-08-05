
==========

简介
-----

安装
-----

# ubuntu
$ sudo apt-get install fabric

注意
-----
使用fab, 需要提前安装fabric.

用法
-----

# filename: 1.py 

def hello():
    print("Hello world!")


$ fab -f 1.py hello



扩展阅读
-------

http://www.fabfile.org/
fab 官网。

In addition to use via the fab tool, Fabric’s components may be imported into other Python code, providing a Pythonic interface to the SSH protocol suite at a higher level than that provided by e.g. the Paramiko library (which Fabric itself uses.)


Fabric is a Python (2.5-2.7) library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks.


fab 文档： 
http://docs.fabfile.org/en/1.6/
简介：



fabric_components 0.1.1
https://pypi.python.org/pypi/fabric_components/0.1.1
简介：
This package contains some common tasks for fabric.




