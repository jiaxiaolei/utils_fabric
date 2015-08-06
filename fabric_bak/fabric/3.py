from fabric.api import local

def test():
    #local('/bin/bash ./a.sh')
    local('cd /home/pabb/; ls')

