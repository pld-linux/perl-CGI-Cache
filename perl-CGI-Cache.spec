#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Cache
Summary:	CGI::Cache perl module
Summary(pl):	Modu³ Perla CGI::Cache
Name:		perl-CGI-Cache
Version:	1.41.2
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fbfffa80c673ac021a70bd45cbfa560b
%if %{with tests}
BuildRequires:	perl-Cache-Cache
BuildRequires:	perl-Tie-Restore
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Cache - Perl extension to help cache output of time-intensive CGI
scripts so that subsequent visits to such scripts will not cost as
much time.

%description -l pl
CGI::Cache - rozszerzenie Perla u³atwiaj±ce buforowanie wyj¶cia z
czasoch³onnych skryptów CGI w ten sposób, ¿e kolejne uruchomienia tych
skryptów bêd± zajmowa³y mniej czasu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo "y" | perl Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/CGI/Cache.pm
%{_mandir}/man3/*
