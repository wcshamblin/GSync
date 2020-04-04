#!/usr/bin/zsh
#tmux send-keys -t "Kiras Kingdom" "say §bBackup commencing..." ENTER
#zip and copy current world to backup folder

###### ONSITE BACKUPS ######
#zip -r /home/mcserver/MCWorlds/ThePearl/`date "+%d-%m-%y-%H:%M"` /home/mcserver/ThePearl
#while [[ "$(ls -l /home/mcserver/MCWorlds/ThePearl/ | wc -l)" -gt 7 ]];do
#        rm "$(ls -1td /home/mcserver/MCWorlds/ThePearl/* | tail -n1)"
#done
############################

###### OFFSITE BACKUPS ######
rclone sync /home/mcserver/ThePearl GDrive:ThePearl -v --backup-dir GDrive:ThePearl`date "+.%d-%m-%y/%R"`/
