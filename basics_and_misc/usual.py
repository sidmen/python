import os

filename = 'send_email.py'
cmd = 'ipconfig'

 cwd = os.getcwd()
find_file = os.path.abspath(filename)
is_file_present = os.path.exists(filename)
is_dir = os.path.isdir(filename)
list_files_dirs = os.listdir(cwd)

print("cwd is '%s'" % cwd)
print("file found at '%s'" % find_file)
print("File exists: %s" % is_file_present)
print("%s is a dir: %s" % (filename, is_dir))
print("%s are the dirs in %s" % (list_files_dirs, cwd))

#############################################################################################

fp = os.popen(cmd)
res = fp.read() # the output of cmd
stat = fp.close() #the exit status
cwd_new = os.getcwd()

print(res)
print(cwd_new)
