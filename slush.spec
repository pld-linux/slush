%define slushversion 0.1.2

Summary: SSL remote access client/server
Name: slush
Version: %{slushversion}
Release: 1
Copyright: GPL
Group: Networking
Source: http://violet.ibs.com.au/slush/files/slush-%{slushversion}.tar.gz
Buildroot: /var/tmp/slush-root

%description
slush is a remote shell system similar to telnet. It uses X509 
certificates for strong authentication instead of passwords and uses 
SSL/TLS for communications security.

%prep

%setup

%build
CFLAGS="-g" ./configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc/slushd
install slushd $RPM_BUILD_ROOT/usr/sbin
install slush $RPM_BUILD_ROOT/usr/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root)
%doc README COPYING COPYRIGHT.GPL COPYRIGHT.SSLeay HISTORY INSTALL README TODO
%doc %attr(0755,root,root) wannabe-ca.sh make-server-cert.sh make-cert.sh hash-certs.sh

%attr(0755,root,root) %dir /etc/slushd

%attr(0700,root,root) /usr/sbin/slushd
%attr(0755,root,root) /usr/bin/slush

%changelog
* Fri May 07 1999 Damien Miller <damien@ibs.com.au>
- Parametised version
- Tries to tweak doc scripts permission

* Thu May 06 1999 Damien Miller <damien@ibs.com.au>
- Created RPM
