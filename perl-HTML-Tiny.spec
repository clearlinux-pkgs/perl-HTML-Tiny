#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTML-Tiny
Version  : 1.05
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/A/AN/ANDYA/HTML-Tiny-1.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AN/ANDYA/HTML-Tiny-1.05.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhtml-tiny-perl/libhtml-tiny-perl_1.05-3.debian.tar.xz
Summary  : Lightweight, dependency free HTML/XML generation
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
HTML-Tiny version 1.05
INSTALLATION
To install this module, run the following commands:

%package dev
Summary: dev components for the perl-HTML-Tiny package.
Group: Development
Provides: perl-HTML-Tiny-devel = %{version}-%{release}

%description dev
dev components for the perl-HTML-Tiny package.


%prep
%setup -q -n HTML-Tiny-1.05
cd ..
%setup -q -T -D -n HTML-Tiny-1.05 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/HTML-Tiny-1.05/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/HTML/Tiny.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTML::Tiny.3
