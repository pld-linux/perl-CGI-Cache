%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Cache
Summary:	CGI::Cache perl module
Summary(pl):	Modu³ perla CGI::Cache
Name:		perl-CGI-Cache
Version:	1.21
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-Cache-Cache
BuildRequires:	perl-Storable
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Cache - Perl extension to help cache output of time-intensive CGI
scripts so that subsequent visits to such scripts will not cost as
much time.

%description -l pl
CGI::Cache - rozszerzenie Perla u³atwiaj±ce buforowanie wyj¶cia z
czasoch³onnych skryptów CGI w ten sposób, ¿e kolejne uruchomienia tych
skrypów bêd± zajmowa³y mniej czasu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo "y" | perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/CGI/Cache.pm
%{_mandir}/man3/*
