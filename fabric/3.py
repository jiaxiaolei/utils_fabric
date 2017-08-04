# -*- coding:utf8 -*-

from fabric.api import local

def test():
	"""本地
	"""
    #local('/bin/bash ./a.sh')
    local('cd /home/pabb/; ls')

