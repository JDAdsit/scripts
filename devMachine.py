#!/usr/bin/python

import sys
import subprocess
import re
import fileinput
		
username = sys.argv[1]

def editHosts():
	filename = '/etc/hosts'
	p = subprocess.call(["sudo", "cp", filename, filename+".backup"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	hostsFile = open(filename, 'a+') 

	hostsFile.write("127.0.0.1       local.solutionreach.com\n")

	hostsFile.write("127.0.0.1       localsites\n\n")

	hostsFile.write("<VirtualHost *:80>\n")
	hostsFile.write("   ServerName local.solutionreach.com\n")
	hostsFile.write("   ServerAlias local.solutionreach.com\n")
	hostsFile.write("   DocumentRoot /Users/"+username+"/Sites/marketing-site\n")
	hostsFile.write("</VirtualHost>\n\n")

	hostsFile.write("<VirtualHost *:80>\n")
	hostsFile.write("   ServerName localhost\n")
 	hostsFile.write("	ServerAlias localhost\n")
	hostsFile.write("   DocumentRoot /Library/WebServer/Documents\n")
	hostsFile.write("</VirtualHost>\n\n")

	hostsFile.write("<VirtualHost *:80>\n")
	hostsFile.write("   ServerName localsites\n")
	hostsFile.write("   ServerAlias localsites\n")
	hostsFile.write("   DocumentRoot /Users/"+username+"/Sites\n")
	hostsFile.write("</VirtualHost>\n")

	hostsFile.close()

# editHosts()


def editHttpdVhosts():
	filename = '/etc/apache2/extra/httpd-vhosts.conf'
	p = subprocess.call(["sudo", "cp", filename, filename+".backup"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	httpdvhostFile = open(filename, 'a+') 

	httpdvhostFile.write("<VirtualHost *:80>\n")
	httpdvhostFile.write("    DocumentRoot '/Users/"+username+"/Sites/marketing-site/'\n")
	httpdvhostFile.write("    ServerName local.solutionreach.com\n")
	httpdvhostFile.write("    Options Indexes FollowSymLinks Includes ExecCGI\n")
	httpdvhostFile.write("</VirtualHost>\n\n")

	httpdvhostFile.write("<VirtualHost *:80>\n")
	httpdvhostFile.write("    #DocumentRoot '/Library/WebServer/Documents'\n")
	httpdvhostFile.write("    DocumentRoot '/Users/"+username+"/Sites/phpMyAdmin'\n")
	httpdvhostFile.write("    ServerName localhost\n")
	httpdvhostFile.write("    Options Indexes FollowSymLinks Includes ExecCGI\n")
	httpdvhostFile.write("</VirtualHost>\n\n")

	httpdvhostFile.write("<VirtualHost *:80>\n")
	httpdvhostFile.write("	DocumentRoot '/Users/"+username+"/Sites'\n")
	httpdvhostFile.write("	ServerName localsites\n")
	httpdvhostFile.write("	Options Indexes FollowSymLinks Includes ExecCGI\n")
	httpdvhostFile.write("</VirtualHost>\n")

	httpdvhostFile.close()

# editHttpdVhosts()

def editusernameconf():
	filename = '/etc/apache2/users/'+username+'.conf'
	p = subprocess.call(["sudo", "cp", filename, filename+".backup"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

	with open(filename, "w") as fout:
		with open(filename+".backup", "r") as fin:
			for line in fin:
				if line == "    Options Indexes MultiViews\n":
					fout.write(line.replace("    Options Indexes MultiViews\n", "    Options Indexes MultiViews FollowSymLinks\n", 1))
				elif line == "    AllowOverride None\n":
					fout.write(line.replace("    AllowOverride None\n", "    AllowOverride All\n", 1))
				else:
					fout.write(line)


# editusernameconf()

def edithttpdconf():
	filename = '/etc/apache2/httpd.conf'
	p = subprocess.call(["sudo", "cp", filename, filename+".backup"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

	with open(filename, "w") as fout:
		with open(filename+".backup", "r") as fin:
			for line in fin:
				if line == "#LoadModule authn_dbm_module libexec/apache2/mod_authn_dbm.so\n":
					fout.write(line.replace("#LoadModule authn_dbm_module libexec/apache2/mod_authn_dbm.so\n", "LoadModule authn_dbm_module libexec/apache2/mod_authn_dbm.so\n", 1))
				elif line == "#LoadModule authn_anon_module libexec/apache2/mod_authn_anon.so\n":
					fout.write(line.replace("#LoadModule authn_anon_module libexec/apache2/mod_authn_anon.so\n", "LoadModule authn_anon_module libexec/apache2/mod_authn_anon.so\n", 1))
				elif line == "#LoadModule authn_dbd_module libexec/apache2/mod_authn_dbd.so\n":
					fout.write(line.replace("#LoadModule authn_dbd_module libexec/apache2/mod_authn_dbd.so\n", "LoadModule authn_dbd_module libexec/apache2/mod_authn_dbd.so\n", 1))
				elif line == "#LoadModule authz_dbm_module libexec/apache2/mod_authz_dbm.so\n":
					fout.write(line.replace("#LoadModule authz_dbm_module libexec/apache2/mod_authz_dbm.so\n", "LoadModule authz_dbm_module libexec/apache2/mod_authz_dbm.so\n", 1))
				elif line == "#LoadModule authz_owner_module libexec/apache2/mod_authz_owner.so\n":
					fout.write(line.replace("#LoadModule authz_owner_module libexec/apache2/mod_authz_owner.so\n", "LoadModule authz_owner_module libexec/apache2/mod_authz_owner.so\n", 1))
				elif line == "#LoadModule authz_dbd_module libexec/apache2/mod_authz_dbd.so\n":
					fout.write(line.replace("#LoadModule authz_dbd_module libexec/apache2/mod_authz_dbd.so\n", "LoadModule authz_dbd_module libexec/apache2/mod_authz_dbd.so\n", 1))
				elif line == "#LoadModule auth_digest_module libexec/apache2/mod_auth_digest.so\n":
					fout.write(line.replace("#LoadModule auth_digest_module libexec/apache2/mod_auth_digest.so\n", "LoadModule auth_digest_module libexec/apache2/mod_auth_digest.so\n", 1))
				elif line == "#LoadModule cache_module libexec/apache2/mod_cache.so\n":
					fout.write(line.replace("#LoadModule cache_module libexec/apache2/mod_cache.so\n", "LoadModule cache_module libexec/apache2/mod_cache.so\n", 1))
				elif line == "#LoadModule dbd_module libexec/apache2/mod_dbd.so\n":
					fout.write(line.replace("#LoadModule dbd_module libexec/apache2/mod_dbd.so\n", "LoadModule dbd_module libexec/apache2/mod_dbd.so\n", 1))
				elif line == "#LoadModule dumpio_module libexec/apache2/mod_dumpio.so\n":
					fout.write(line.replace("#LoadModule dumpio_module libexec/apache2/mod_dumpio.so\n", "LoadModule dumpio_module libexec/apache2/mod_dumpio.so\n", 1))
				elif line == "#LoadModule ext_filter_module libexec/apache2/mod_ext_filter.so\n":
					fout.write(line.replace("#LoadModule ext_filter_module libexec/apache2/mod_ext_filter.so\n", "LoadModule ext_filter_module libexec/apache2/mod_ext_filter.so\n", 1))
				elif line == "#LoadModule include_module libexec/apache2/mod_include.so\n":
					fout.write(line.replace("#LoadModule include_module libexec/apache2/mod_include.so\n", "LoadModule include_module libexec/apache2/mod_include.so\n", 1))
				elif line == "#LoadModule substitute_module libexec/apache2/mod_substitute.so\n":
					fout.write(line.replace("#LoadModule substitute_module libexec/apache2/mod_substitute.so\n", "LoadModule substitute_module libexec/apache2/mod_substitute.so\n", 1))
				elif line == "#LoadModule deflate_module libexec/apache2/mod_deflate.so\n":
					fout.write(line.replace("#LoadModule deflate_module libexec/apache2/mod_deflate.so\n", "LoadModule deflate_module libexec/apache2/mod_deflate.so\n", 1))
				elif line == "#LoadModule log_forensic_module libexec/apache2/mod_log_forensic.so\n":
					fout.write(line.replace("#LoadModule log_forensic_module libexec/apache2/mod_log_forensic.so\n", "LoadModule log_forensic_module libexec/apache2/mod_log_forensic.so\n", 1))
				elif line == "#LoadModule logio_module libexec/apache2/mod_logio.so\n":
					fout.write(line.replace("#LoadModule logio_module libexec/apache2/mod_logio.so\n", "LoadModule logio_module libexec/apache2/mod_logio.so\n", 1))
				elif line == "#LoadModule mime_magic_module libexec/apache2/mod_mime_magic.so\n":
					fout.write(line.replace("#LoadModule mime_magic_module libexec/apache2/mod_mime_magic.so\n", "LoadModule mime_magic_module libexec/apache2/mod_mime_magic.so\n", 1))
				elif line == "#LoadModule expires_module libexec/apache2/mod_expires.so\n":
					fout.write(line.replace("#LoadModule expires_module libexec/apache2/mod_expires.so\n", "#LoadModule expires_module libexec/apache2/mod_expires.so\n", 1))
				elif line == "#LoadModule usertrack_module libexec/apache2/mod_usertrack.so\n":
					fout.write(line.replace("#LoadModule usertrack_module libexec/apache2/mod_usertrack.so\n", "LoadModule usertrack_module libexec/apache2/mod_usertrack.so\n", 1))
				elif line == "#LoadModule userdir_module libexec/apache2/mod_userdir.so\n":
					fout.write(line.replace("#LoadModule userdir_module libexec/apache2/mod_userdir.so\n", "LoadModule userdir_module libexec/apache2/mod_userdir.so\n", 1))
				elif line == "#LoadModule rewrite_module libexec/apache2/mod_rewrite.so\n":
					fout.write(line.replace("#LoadModule rewrite_module libexec/apache2/mod_rewrite.so\n", "LoadModule rewrite_module libexec/apache2/mod_rewrite.so\n", 1))
				elif line == "#LoadModule php5_module libexec/apache2/libphp5.so\n":
					fout.write(line.replace("#LoadModule php5_module libexec/apache2/libphp5.so\n", "LoadModule php5_module libexec/apache2/libphp5.so\n", 1))
				elif line == "User _www\n":
					fout.write(line.replace("User _www\n", "User "+username+"\n", 1))
				elif line == "Group _www\n":
					fout.write(line.replace("Group _www\n", "Group staff\n", 1))
				elif line == "    AllowOverride none\n":
					fout.write(line.replace("    AllowOverride none\n", "    AllowOverride All\n", 1))
				elif line == "    AllowOverride None\n":
					fout.write(line.replace("    AllowOverride None\n", "    AllowOverride All\n", 1))
				elif line == "    Require all denied\n</Directory>":
					fout.write(line.replace("    Require all denied\n</Directory>", "    Options Indexes FollowSymLinks Includes ExecCGI\n    Order deny,allow\n    Allow from all\n", 1))
				elif line == 'DocumentRoot "/Library/WebServer/Documents"\n':
					fout.write(line.replace('DocumentRoot "/Library/WebServer/Documents"\n', 'DocumentRoot "/Users/'+username+'/Sites"\n', 1))
				elif line == '<Directory "/Library/WebServer/Documents">\n':
					fout.write(line.replace('<Directory "/Library/WebServer/Documents">\n', '<Directory "/Users/'+username+'/Sites">\n', 1))
				else:
					fout.write(line)


# edithttpdconf()

def createDB():
	p = subprocess.call(["sudo", "mysql", "-u", "root", "-p", "pass", "solre", "<", "dump.sql"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# createDB()

def phpmyadmin():
	p = subprocess.call(["tar", "xopf", "phpMyAdmin-4.3.8-english.tar.gz"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	p = subprocess.call(["sudo", "chmod", "-R", "777", "phpMyAdmin-4.3.8-english/"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

	filename = 'phpMyAdmin-4.3.8-english/config.inc.php'
	filenameIn = 'phpMyAdmin-4.3.8-english/config.sample.inc.php'
	p = subprocess.call(["sudo", "cp", filenameIn, filename], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

	with open(filename, "w") as fout:
		with open(filenameIn, "r") as fin:
			for line in fin:
				if line == "$cfg['Servers'][$i]['AllowNoPassword'] = false;\n":
					fout.write(line.replace("$cfg['Servers'][$i]['AllowNoPassword'] = false;\n", "$cfg['Servers'][$i]['AllowNoPassword'] = false;\n$cfg['Servers'][$i]['user'] = 'root';\n$cfg['Servers'][$i]['password'] = 'pass';\n", 1))
				else:
					fout.write(line)

	p = subprocess.call(["mv", "phpMyAdmin-4.3.8-english", "/Users/"+username+"/Sites/phpMyAdmin1"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

phpmyadmin();