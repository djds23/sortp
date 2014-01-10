#sort photos in directories
import os
import re
import shutil

identifier=r'fin_'

contents = [files for files in os.listdir('.') if re.match(identifier, files) != None]
if contents and 'Final' not in os.listdir('.'):
	os.mkdir('Final')
	move = [shutil.move(files, 'Final') for files in contents]
	exit()
print  'Nothing is marked %s yet! Either that or Final already exists...' % identifier