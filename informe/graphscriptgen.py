import os, fnmatch

def locate(pattern, root=os.curdir):
    '''Locate all files matching supplied filename pattern in and below
    supplied root directory.'''
    for path, dirs, files in os.walk(os.path.abspath(root)):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)

def main():
	for filepath in locate('*-result.out', '..'):
		file = os.path.basename(filepath)
		print "set output '%s.png'" % file
		print "plot '%s' using ($2 + 1/($3 == 1)) t 'Perdio', '%s' using ($2 + 1/($3 == 3)) t 'Gano'" % (filepath, filepath)
		print

main()