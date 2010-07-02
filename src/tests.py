# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kula"
__date__ ="$2010-6-10 20:50:38$"

import doctest
if __name__ == '__main__':
    optionflags = doctest.ELLIPSIS
    doctest.testfile("readme.txt",optionflags = doctest.ELLIPSIS)