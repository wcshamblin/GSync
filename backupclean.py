#!/usr/bin/python3
import os
import datetime
days=5 #older than days, delete
ddel=3 #if less than ddel backups are found of directory, don't delete any
def datedif(d0, d1, dateformat):
    d0 = datetime.datetime.strptime(d0, dateformat)
    d1 = datetime.datetime.strptime(d1, dateformat)
    return abs((d1-d0).days)
tree=os.popen("rclone lsd GDrive: --max-depth 1 | awk '{print $5}'").read().strip()
dformat = '%d-%m-%y'
today=datetime.date.today()
today = str(today.strftime(dformat))
dirs=[]
delbuf=[]
for line in tree.split("\n")[:-2]:
    dirs.append(line)
for line in dirs:
    dateline=line.split(".")
    if len(dateline)>1 and sum(dir.startswith(dateline[0]) for dir in dirs)>ddel:
        if datedif(today, dateline[1], dformat)>days:
            delbuf.append(line)

print("All directories:", dirs)

print("To be deleted:", delbuf)
for dir in delbuf:
    os.system("rclone delete GDrive:"+dir+"/")
    os.system("rclone rmdirs GDrive:"+dir+"/")
