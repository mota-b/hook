# imports
import os
import sys
import gens_list
import re

nb_args = len(sys.argv)
args = sys.argv
g_list = gens_list.gens


# controle args number
if nb_args == 1:
    print "-Error- insuffisant arguments"
else:

    # controle the path
    path_given = args[1]
    dest = re.findall(r'(^./[\w/@-]*)|^[.]$', path_given, re.UNICODE)
    if len(dest)== 0 :
        print "-Error- Wrong path"
    else:
        if len(dest) == 1 and dest[0]=="":
            dest = os.getcwd() + "/"
        else:
            dest = os.getcwd() + dest[0].split(".")[1] +"/"
        
        # controle generator
        generator = args[2]
        v = False
        for gen in g_list:
            if generator == gen["call"]:
                v = True
                gen_index = g_list.index(gen)
                break
        if v == False :
            print "-Error- unhundled generator"
        else:
            
            # call the proper generator 
            from importlib import import_module
            generator_name = g_list[gen_index]["name"]
            gn = import_module("Generators." + generator_name + "." + generator_name)
            
            # generate
            gn.gen(g_list[gen_index], dest, args[3:len(args)])
            

    
   
    
