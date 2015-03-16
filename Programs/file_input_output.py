# read - file reading mode; keeps current file in tact and reads from it.
# write - write to a file; destroys current file and writes new information.
# binary - binary read/write access.
# append - writes to file; keeps current file and adds to the end of it.

fh = open('TheHulk.txt', 'w') # open a file for writing
fh.write('HULK SMASH')
fh.close()

fh = open('TheHulk.txt', 'r') # open a file for reading
text = fh.read()
fh.close()

fh = open('TheHulk.txt', 'a')
fh.write('\nPUNY MAN')
fh.close()