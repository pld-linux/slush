Summary:	SSL remote access client/server
Name:		slush
Version:	0.1.2
Release:	1
Copyright:	GPL
Group:		Networking
Source:		http://violet.ibs.com.au/slush/files/%{name}-%{version}.tar.gz
BuildRequires:	openssl-devel >= 0.9.4-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
slush is a remote shell system similar to telnet. It uses X509 
certificates for strong authentication instead of passwords and uses 
SSL/TLS for communications security.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_bindir},%{_sbindir},/etc/slushd}
install slushd $RPM_BUILD_ROOT/%{_sbindir}
install slush $RPM_BUILD_ROOT/%{_bindir}

gzip -9nf README HISTORY README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,HISTORY,README,TODO}.gz
%doc %attr(755,root,root) wannabe-ca.sh make-server-cert.sh make-cert.sh hash-certs.sh
%dir /etc/slushd
%attr(700,root,root) /usr/sbin/slushd
%attr(755,root,root) /usr/bin/slush
