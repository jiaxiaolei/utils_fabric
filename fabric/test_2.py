from fabric.api import local

"""Usage

$ fab -f 2.py test
"""

def test(): 
    """A test script.

    $ fab -f 2.py test	
    """
    #local('/bin/bash ./a.sh')
    local('/bin/bash ./b.sh')

