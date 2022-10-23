import os.path

def txt_to_tuple(file_dir:str) -> tuple():
    result = []
    f = open(file_dir, 'r')
    for line in f:
        line=line[:-1]
        array=line.split()
        result.append((array[0],int(array[1])))
    return result




