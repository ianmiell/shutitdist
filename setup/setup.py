"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class setup(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.install('build-essential')
		shutit.install('curl')
		shutit.install('libcurl4-gnutls-dev')
		shutit.install('libpcre3-dev') # required as the hand-built one causes problems at pango
		shutit.install('libssl-dev') # for openssl includes, for git
		shutit.install('m4') # do we need this?
		shutit.remove('libxml2') # old version
		#shutit.install('strace') # remove later, for debug
		#shutit.install('xterm') # remove later, for debug (resize)
		# libglib2.0-0 #libglib2.0-0:amd64 #libglib2.0-data # REMOVE?
		shutit.send('echo "ShutIt Distro version 0.1" > /etc/issue')
		# Some builds expect head in /bin
		shutit.send('mv -v /usr/bin/head /bin/head')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	#def finalize(self, shutit):
	#	return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return setup(
		'shutit.tk.sd.setup.setup', 158844782.0003,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)

