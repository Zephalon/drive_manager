
# Housekeeping

## Drive Manager

A simple Python script that deletes redundant files if the reserved disk space is exceeded.

# How To Run

To run it once, simply run the python script:

    sudo python3 drive_manager.py

To  run the script automatically at a specified interval open crontab:

    sudo crontab -e

... and run it for example daily at midnight by adding:

    0 0 * * * /usr/bin/python /my_path/drive_manager.py
