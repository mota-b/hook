import re 
import os

def gen(gen_object, path, args):

    # controle options
    option = args[0]
    v = False
    for op in gen_object["options"]:
        if op == option:
            v = True
            op_index = gen_object["options"].index(option)
            break
    if v == False :
        print "-Error- (",option, ") is unhundled in ",gen_object["call"]
    else:

        # controle the file name
        file_name = re.findall(r"^"+gen_object["comp_pattern"]+"$", args[1])
        if len(file_name) == 0:
            print "-Error- unhundled File-name"
        else:
            file_name = file_name[0]
            
             # generate the file from options
            filedest = open( path + file_name + ".jsx", "w")

            fl_model_path = os.path.dirname(os.path.realpath(__file__))+"/Models/"+gen_object["call"]+option+".txt"
            file_model = open(fl_model_path, "r")

            buffer = file_model.read()
            buffer = buffer.replace(r"C_name", file_name)
            filedest.write(buffer)

            file_model.close()
            filedest.close()