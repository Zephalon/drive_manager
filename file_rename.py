import re, os, shutil

# setup
input_path = '/video/inbox'
output_path_tvshow = '/video/tv_show'
output_path_movie = '/video/movie'
special_chars = '._+' # replace these characters with empty spaces
video_file_extensions = ['.mp4', '.mkv'] # only touch files with these extensions

files = []

# iterate directory
for file_name in os.listdir(input_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(input_path, file_name)):
        files.append(file_name)

print(files)

for file_name in files:
    name, file_extension = os.path.splitext(file_name)

    if file_extension in video_file_extensions:

        for special_char in special_chars:
            name = name.replace(special_char, ' ')

        splinters = re.split("[sS](\d\d?)[eE](\d\d?)", name)
        
        if (len(splinters) > 1):
            # should be a tv show
            new_filename = splinters[0].replace('Watch ', '').strip().title()
            new_filename += ' S' + splinters[1] + 'E' + splinters[2] + file_extension

            print(file_name + ' => ' + new_filename)

            shutil.move(input_path + '/' + file_name, output_path_tvshow + '/' + new_filename)
        else:
            # should be a movie
            result = re.findall("360|480|720|1080|2160", name)
            splinters = re.split("360|480|720|1080|2160", name)
            new_filename = splinters[0].strip().title()

            if (result): new_filename += ' (' + result[0] + 'p)'

            new_filename += file_extension

            print(file_name + ' => ' + new_filename)

            shutil.move(input_path + '/' + file_name, output_path_movie + '/' + new_filename)