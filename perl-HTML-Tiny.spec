#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-HTML-Tiny
Version  : 1.08
Release  : 35
URL      : https://cpan.metacpan.org/authors/id/A/AR/ARISTOTLE/HTML-Tiny-1.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AR/ARISTOTLE/HTML-Tiny-1.08.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhtml-tiny-perl/libhtml-tiny-perl_1.05-3.debian.tar.xz
Summary  : 'Lightweight, dependency free HTML/XML generation'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTML-Tiny-license = %{version}-%{release}
Requires: perl-HTML-Tiny-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
HTML::Tiny
"HTML::Tiny" is a simple, dependency free module for generating HTML
(and XML). It concentrates on generating syntactically correct XHTML
using a simple Perl notation.

%package dev
Summary: dev components for the perl-HTML-Tiny package.
Group: Development
Provides: perl-HTML-Tiny-devel = %{version}-%{release}
Requires: perl-HTML-Tiny = %{version}-%{release}

%description dev
dev components for the perl-HTML-Tiny package.


%package license
Summary: license components for the perl-HTML-Tiny package.
Group: Default

%description license
license components for the perl-HTML-Tiny package.


%package perl
Summary: perl components for the perl-HTML-Tiny package.
Group: Default
Requires: perl-HTML-Tiny = %{version}-%{release}

%description perl
perl components for the perl-HTML-Tiny package.


%prep
%setup -q -n HTML-Tiny-1.08
cd %{_builddir}
tar xf %{_sourcedir}/libhtml-tiny-perl_1.05-3.debian.tar.xz
cd %{_builddir}/HTML-Tiny-1.08
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/HTML-Tiny-1.08/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTML-Tiny
cp %{_builddir}/HTML-Tiny-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-HTML-Tiny/638f7659729eedb5f661a01eb99a5e81d6e9f451 || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-HTML-Tiny/197f9c6c44d34d00c6953817b7e11154f2bcb75e || :
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTML::Tiny.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTML-Tiny/197f9c6c44d34d00c6953817b7e11154f2bcb75e
/usr/share/package-licenses/perl-HTML-Tiny/638f7659729eedb5f661a01eb99a5e81d6e9f451

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
