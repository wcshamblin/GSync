#!/usr/bin/python3
import argparse
import os
from datetime import datetime, date
ps = argparse.ArgumentParser(description='Sync\'s <path> with <remote>')
ps.add_argument("path", type=str, help='Path to folder to be uploaded/sync\'d to remote')
ps.add_argument("remote", type=str, help='RClone remote folder (Remote: or Remote:Folder)')
ps.add_argument("-c", "--clean", action="store_true", help="Clean old files (see -c, -e)")
ps.add_argument("-f", "--flags", type=str, help="Extra rclone flags to be passed (see rclone docs)")
ps.add_argument("-e", "--expire", type=int, help="Expiry date - if older than <num> days, delete (defaults to 5)")
ps.add_argument("-k", "--keep", type=int, help="If less than <num> backups of directory are found, don't delete any (defaults to 3)")

args=ps.parse_args()
remote=args.remote.split(':')[1]
if remote!='':
	if not args.clean:
		args.remote=(args.remote+'/'+remote)
else:
	dirs=[directory for directory in args.path.split('/') if directory]
	if args.clean:
		args.remote=args.remote+dirs[-1]
	else:
		args.remote=args.remote+dirs[-1]+'/'+dirs[-1]
if args.flags:
	eargs=args.flags
else:
	eargs=''
if args.clean:
	days=5 #older than days, delete
	ddel=3 #if less than ddel backups are found of directory, don't delete any
	if args.expire:
		days=args.expire
	if args.keep:
		ddel=args.keep
	def datedif(d0, d1, dateformat):
		d0 = datetime.strptime(d0, dateformat)
		d1 = datetime.strptime(d1, dateformat)
		return abs((d1-d0).days)
	tree=os.popen("rclone lsd "+str(args.remote)+" --max-depth 1 | awk '{print $5}'").read().strip()
	dformat = '%d-%m-%y'
	today=date.today()
	today = str(today.strftime(dformat))
	dirs=[]
	delbuf=[]
	for line in tree.split("\n"):
		dirs.append(line)
	for line in dirs:
		dateline=line.split(".")
		if len(dateline)>1 and sum(dir.startswith(dateline[0]) for dir in dirs)>ddel:
		    if datedif(today, dateline[1], dformat)>days:
		        delbuf.append(line)

	print("All directories:", dirs)

	print("To be deleted:", delbuf)
	for dir in delbuf:
		os.system("rclone delete GDrive:"+dir+"/"+' '+eargs)
		os.system("rclone rmdirs GDrive:"+dir+"/"+' '+eargs)
else:
	os.system("rclone sync "+args.path.rstrip('/')+' '+args.remote+" -v --backup-dir "+args.remote+'-'+datetime.now().strftime('%Y-%m-%d/%R')+' '+eargs)