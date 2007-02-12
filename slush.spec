Summary:	SSL remote access client/server
Summary(pl.UTF-8):	Klient/serwer zdalnego dostępu po SSL
Name:		slush
Version:	0.1.2
Release:	1
License:	GPL
Group:		Networking
Source0:	http://violet.ibs.com.au/slush/files/%{name}-%{version}.tar.gz
# Source0-md5:	7bf760806295d4df3247fc7bbdb351db
BuildRequires:	autoconf
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
slush is a remote shell system similar to telnet. It uses X509
certificates for strong authentication instead of passwords and uses
SSL/TLS for communications security.

%description -l pl.UTF-8
slush jest systemem zdalnej powłoki podobnym do telnetu. Używa
certyfikatów X.509 do silnej autentykacji zamiast haseł i używa
SSL/TLS dla bezpiecznej komunikacji.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_sysconfdir}/slushd}

install slushd $RPM_BUILD_ROOT%{_sbindir}
install slush $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HISTORY TODO
%doc %attr(755,root,root) wannabe-ca.sh make-server-cert.sh make-cert.sh hash-certs.sh
%dir %{_sysconfdir}/slushd
%attr(700,root,root) %{_sbindir}/slushd
%attr(755,root,root) %{_bindir}/slush
