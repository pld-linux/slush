Summary:	SSL remote access client/server
Summary(pl):	Klient/serwer zdalnego dostêpu po SSL
Name:		slush
Version:	0.1.2
Release:	1
License:	GPL
Group:		Networking
Source0:	http://violet.ibs.com.au/slush/files/%{name}-%{version}.tar.gz
BuildRequires:	openssl-devel >= 0.9.4-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
slush is a remote shell system similar to telnet. It uses X509
certificates for strong authentication instead of passwords and uses
SSL/TLS for communications security.

%description -l pl
slush jest systemem zdalnej pow³oki podobnym do telnetu. U¿ywa
certyfikatów X.509 do silnej autentykacji zamiast hase³ i u¿ywa
SSL/TLS dla bezpiecznej komunikacji.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_bindir},%{_sbindir},%{_sysconfdir}/slushd}
install slushd $RPM_BUILD_ROOT/%{_sbindir}
install slush $RPM_BUILD_ROOT/%{_bindir}

gzip -9nf README HISTORY README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,HISTORY,README,TODO}.gz
%doc %attr(755,root,root) wannabe-ca.sh make-server-cert.sh make-cert.sh hash-certs.sh
%dir %{_sysconfdir}/slushd
%attr(700,root,root) %{_sbindir}/slushd
%attr(755,root,root) %{_bindir}/slush
