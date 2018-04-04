import fileinput

for line in fileinput.input('nginx.conf', backup='.bak', inplace=1):


