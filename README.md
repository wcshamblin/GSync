# GSync.py
GSync provides revision control for rclone remote's without it (Most notably Google Drive, lacking folder revision control)

## Installation
```bash
chmod 755 ./GSync.py
```
Then put appropriate running times in your crontab file for both syncing and cleaning.
See
```bash
./GSync.py --help
```
for more info.

## Caveats
Backup directory's timestamp is the time when it was *copied*, not when the backup was actually created.
For example, if your backup cronjob runs every 1 day, backups will actually appear one day newer than they actually are.
