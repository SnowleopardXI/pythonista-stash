# -*- coding: utf-8 -*-

import os
command_list = 'pip list' 
command_install = 'pip install '
data = os.popen(command_list) 
info = data.readlines() 
del info[0]
del info[0]
for line in info:  
    package = line.split(" ")[0]
    print("",end="")
    print("\033[1;32;40m%s\033[0m"%("Checking updates"+package))
    os.system(command_install+package+" --upgrade")
print("All done")

