# GSync
GSync syncs backups to an rclone remote directory, and automatically deletes old backups

## Installation
```bash
chmod 755 ./backupclean.py ./backupbuffer.sh
```
Then put appropriate running times in your crontab file for both the backup script and the cleaning script.

## Caveats
Backup directory's timestamp is the time when it was *copied*, not when the backup was actually created.
For example, if your backup cronjob runs every 1 day, backups will actually appear one day newer than they actually are.





Report bugs to: will@shamblin.org
