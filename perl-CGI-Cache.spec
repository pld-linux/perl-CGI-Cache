%include	/usr/lib/rpm/macros.perl
Summary:	CGI-Cache perl module
Summary(pl):	Modu³ perla CGI-Cache
Name:		perl-CGI-Cache
Version:	1.03
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-Cache-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-Cache - Perl extension to help cache output of time-intensive CGI
scripts so that subsequent visits to such scripts will not cost as
much time.

%description -l pl
Modu³ perla CGI-Cache.

%prep
%setup -q -n CGI-Cache-%{version}

%build
echo "y" | perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/CGI/Cache.pm
%{_mandir}/man3/*
