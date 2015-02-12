import sys
import subprocess

username = sys.argv[1]

def undoBackup(filename):
	p = subprocess.call(["sudo", "rm", filename], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	p = subprocess.call(["sudo", "mv", filename+".backup", filename], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# undoBackup('/etc/hosts')
# undoBackup('/etc/apache2/extra/httpd-vhosts.conf')
# undoBackup('/etc/apache2/httpd.conf')
# undoBackup('/etc/apache2/users/'+username+'.conf')