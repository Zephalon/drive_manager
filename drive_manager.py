import time, os, stat, shutil

def fileAgeInDays(pathname):
    return round((time.time() - os.stat(pathname)[stat.ST_MTIME]) / 60 / 60 / 24)

def bytesTo(bytes, to, bsize=1024): 
    a = {'k' : 1, 'm': 2, 'g' : 3, 't' : 4, 'p' : 5, 'e' : 6 }
    r = float(bytes)
    return round(bytes / (bsize ** a[to]), 2)

# setup
drive_path = '/media/nas'
dir_path = drive_path + '/video'
required_disk_space = 500 # in GiB
maximum_file_age = 90 # in days, set to 'False' to disable it

total, used, free = shutil.disk_usage(drive_path)

print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))
print("Required: %d GiB" % required_disk_space)

free_space = free // (2**30)
space_to_freed =  required_disk_space - free_space

# lists to store files
files = {}
files_to_delete = []
freed_space = 0

# iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        files[path] = fileAgeInDays(dir_path + '/' + path)

files = dict(sorted(files.items(), key=lambda item: item[1], reverse=True)) # sort files by age

# free drive space
if (space_to_freed > 0):
    print("Disk Space To Be Freed: %d GiB" % space_to_freed)

    # mark files for deletion until enough space is freed
    while(space_to_freed > 0):
        for file in sorted_files:
            space_to_freed -= bytesTo(os.stat(dir_path + '/' + path).st_size, 'g')
            files_to_delete.append(file)
else:
    print("Disk Space Left: %d GiB" % abs(space_to_freed))

# delete old files
if (maximum_file_age != False):
    for file in files:
        if (files[file] >= maximum_file_age):
            files_to_delete.append(file)

print("Files To Be Deleted:")
print(files_to_delete)

# entering the danger zone
for file_path in files_to_delete:
    os.remove(dir_path + '/' + file_path)
    freed_space += bytesTo(os.stat(dir_path + '/' + file_path).st_size, 'g')

print("Files Deleted, Space Freed: %d GiB" % freed_space)