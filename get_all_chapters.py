with open('chapters_out_link') as f :
    file=f.readlines()
for i in file :
    i=i.strip()
    print i.split("\"")[1]