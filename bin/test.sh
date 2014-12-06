#!/bin/bash
if [[ $1 = '' ]]
then
	start="setup"
	started="1"
else
	start="$1"
	started="0"
fi
pushd ..
find . | grep .cnf$ | xargs chmod 0600
popd
# TODO berkeleydb
for d in setup bzip2 tcl autoconf gperf icu sqlite which gmp lzo onigurama flex xmlto gettext automake libffi libidn texinfo util_macros expat zlib apache_portable_runtime pkg_config openssl procps_ng openjade cpio libssl zip python2 wget ncurses readline llvm asciidoc help2man libxml2 python_pip nettle tls libarchive libxslt docbookxml docbookxsl apache_portable_runtime_util scons cmake serf subversion gmp git libtool jq sthttpd kona go xcb_proto libxau linuxbrew libpng libxcb glib harfbuzz pcre rsync gawk sgml_common bison groff docbook vim lxml inetutils yacc libxslt iproute2 less giflib sudo x7proto alsa_lib libxau linuxbrew libpng freetype freetype2 desktop_file_utils fontconfig opensp docbook_dsssl docbook_sgml_dtd docbook_utils xorg_libs atk cups nasm libjpeg libtiff gdk_pixbuf pixman cairo pango gtk2 lcms 
do
	if [[ $started = "0" ]]
	then
		if [[ $start = $d ]]
		then
			started="1"
		else
			continue
		fi
	fi
	pushd ../$d/bin
	echo $(date)
	echo $d BEGIN
	./build_and_push.sh > /tmp/shutitdistout 2>&1
	if [[ $? != 0 ]]
	then
		echo FAILED
		exit 1
	fi
	echo $(date)
	echo $d DONE
	popd
done

