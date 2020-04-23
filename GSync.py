#!/usr/bin/python3
import argparse
import os
from datetime import datetime
ps = argparse.ArgumentParser(description='Sync\'s <path> with <remote>')
ps.add_argument("path", type=str, help='Path to folder to be sync\'d')
ps.add_argument("remote", type=str, help='RClone remote folder (Remote:Folder)')
ps.add_argument("-f", "--flags", type=str, help="Extra rclone flags to be passed (see rclone docs)")
args=ps.parse_args()
datetime.now().strftime('%Y-%m-%d')
remote=args.remote.split(':')[1]
if remote!='':
	args.remote=(args.remote+'/'+remote)
else:
	dirs=[directory for directory in args.path.split('/') if directory]
	args.remote=args.remote+dirs[-1]+'/'+dirs[-1]
if args.flags:
	eargs=args.flags
else:
	eargs=''
os.system("rclone sync "+args.path.rstrip('/')+' '+args.remote+" -v --backup-dir "+args.remote+'-'+datetime.now().strftime('%Y-%m-%d/%R')+' '+eargs)