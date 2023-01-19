import os
import shutil
from pathlib import Path
images, docs, videos, archives, apps, folders, music= 0,0,0,0,0,0,0
path_dir = os.path.dirname(os.path.realpath(__file__))
for filename in os.listdir(path_dir):

    if filename.endswith((".jpg",".png","jpeg")):
        if not os.path.exists("Images"):
           os.makedirs("Images")
        shutil.move(filename, "Images")
        images +=1
        continue

    if filename.endswith((".mp4")):
        if not os.path.exists("videos"):
           os.makedirs("videos")
        shutil.move(filename, "videos")
        videos +=1
        continue


    if filename.endswith((".pdf",".word")):
        if not os.path.exists("Docs"):
           os.makedirs("Docs")
        shutil.move(filename, "Docs")
        docs +=1
        continue

    if filename.endswith((".zip",".rar")):
        if not os.path.exists("archives"):
           os.makedirs("archives")
        shutil.move(filename, "archives")
        archives +=1
        continue

    if filename.endswith((".exe",".dmg")):
        if not os.path.exists("apps"):
           os.makedirs("apps")
        shutil.move(filename, "apps")
        apps +=1
        continue

    if filename.count(".") > 0:
        ext = filename.split(".")[-1]
        newfile = path_dir  + "\\" + ext
        if not os.path.exists(newfile):
            os.makedirs(newfile)
            folders +=1
        source = path_dir + "\\" + filename 
        destination = path_dir + "\\" + ext
        shutil.move(source, destination)

print("images: {}, music: {}, videos: {}, apps: {}, archives: {}, docs: {}, others: {}".format(images,music,videos,apps,archives,docs,folders+5))
