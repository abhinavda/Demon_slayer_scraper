import commands

user="<your username on laptop>"
root_dir="/Users/%s/projects/dumps/comics/demon_slayer"%user

dirs= commands.getoutput("ls %s"%root_dir).split()
# print dirs[1]
# print len(dirs)

for each_dir in dirs[:] :
    try :
        cmd="ls %s/%s"%(root_dir,each_dir)
        cmd_out=commands.getoutput(cmd)
        rest_vals=cmd_out.split("\n")[-1].split("_")[1:] #['1', '60.jpg'] or ['010-020.png']
        max_count_page = 0
        for x in cmd_out.split("\n"):
            x = x.split("_")
            if len(x) == 1:
                num_pages = x[0].split("-")[-1].split(".")[0]
            else:
                num_pages = x[-1].split("-")[-1]
            # print num_pages.split(".")[0]
            temp_count = int(num_pages.split(".")[0])
            # print temp_count
            if temp_count > max_count_page:
                max_count_page = temp_count
        #print max_count_page
        total_files=len(cmd_out.split("\n"))
        #print final_page,total_files
        if max_count_page!=total_files or max_count_page < 19 :
            print each_dir
            print max_count_page,total_files
            print
    except :
        print "error for %s"%each_dir
