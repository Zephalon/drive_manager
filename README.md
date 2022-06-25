# Housekeeping

A collection of useful Python scripts for my home server.

## drive_manager.py

A Python script that deletes redundant files if the reserved disk space is exceeded.

### How To Run

To run it once, simply run the python script:

    sudo python3 drive_manager.py

To  run the script automatically at a specified interval open crontab:

    sudo crontab -e

... and run it (for example) daily at midnight by adding:

    0 0 * * * /usr/bin/python /my_path/drive_manager.py

## file_rename.py

A Python script that renames video files and moves them to another folder.

### How To Run

Similar to the drive manager you should add it to the cronjobs with a fitting interval.