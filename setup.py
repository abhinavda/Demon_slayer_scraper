import os
user="<your username on laptop>"
parent_dir="/Users/%s/projects/dumps/comics/demon_slayer"%user
file_arr=[]
with open('chapters_only_link') as f :
    file=f.readlines()
    for i in file :
        i=i.strip()
        temp_file="-".join(i.split("/")[-1].split("-")[5:])
        file_arr.append(temp_file)
for directory in file_arr[2:] :
    path = os.path.join(parent_dir, directory)
    print directory
    os.mkdir(path)
