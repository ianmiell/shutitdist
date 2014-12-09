"""ShutIt module. See http://shutit.tk """

from shutit_module import ShutItModule


class curl(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/curl')
		shutit.send('cd /tmp/build/curl')
		shutit.send('curl -L http://curl.haxx.se/download/curl-7.39.0.tar.gz | tar -zxf -')
		shutit.send('cd curl*')
		shutit.send('apt-get -y purge curl') # actually destroy all trace of curl from /usr
		shutit.send('./configure --prefix=/usr --disable-static --enable-threaded-resolver --without-ssl  --with-gnutls')
		shutit.send('make')
		shutit.send('make install')
		#shutit.send('find /usr | grep -w curl | xargs rm -rf') # actually destroy all trace of curl from /usr
		#shutit.send('find /usr | grep libcurl | xargs rm -rf') # actually destroy all trace of curl from /usr
		# Remove the old libssl
		shutit.send('rm -f /usr/lib/x86_64-linux-gnu/libssl.so.1.0.0')
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
	return curl(
		'shutit.tk.sd.curl.curl', 158844782.00805,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.tls.tls','shutit.tk.sd.libssl.libssl']
	)

