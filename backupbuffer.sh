#!/usr/bin/bash
LDIR='/path/to/dir/'    #local directory
RDIR='GDrive:Directory' #rclone remote:directory
rclone sync $LDIR $RDIR -v --backup-dir $RDIR`date "+.%d-%m-%y/%R"`/
