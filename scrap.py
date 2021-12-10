#!/bin/python

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time,sys,os,urllib
from selenium.webdriver.common.action_chains import ActionChains

#broswer_url="https://ww5.demonslayermanga.com/chapter/demon-slayer-kimetsu-no-yaiba-chapter-2"
#root_dir="/Users/<user>/projects/dumps/comics/demon_slayer/chapter-2/"

browser = webdriver.Chrome(ChromeDriverManager().install())
user="<your username on laptop>"

def open_webpage(broswer_url) :
    try :
        browser.get(broswer_url)
        time.sleep(3)
        #print browser.page_source
        all_images=(browser.page_source).split("\n")
        root_dir="/Users/%s/projects/dumps/comics/demon_slayer/"%user
        for i in all_images[:] :
            if i.strip()[:4]=="<img" :
                print i.strip().split("\"")[1]
                link=i.strip().split("\"")[1]
                temp_file = "-".join(str(broswer_url).split("/")[-1].split("-")[5:])
                image_name=str(link).strip().split("/")[-1]
                file_name=root_dir+temp_file+"/"+image_name
                print file_name
                os.system('wget -O %s %s'%(file_name,link))
                time.sleep(3)

        #return
    except Exception as e:
        print e, "Manga website couldn't be opened."
        #return

with open("chapters_only_link") as f :
    file=f.readlines()
    for i in file[:] :
        i=i.strip()
        open_webpage(i)
        time.sleep(2)
browser.close()
