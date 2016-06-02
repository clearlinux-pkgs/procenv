#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : procenv
Version  : 0.46
Release  : 7
URL      : https://github.com/jamesodhunt/procenv/archive/0.46.tar.gz
Source0  : https://github.com/jamesodhunt/procenv/archive/0.46.tar.gz
Summary  : Utility to show process environment
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: procenv-bin
Requires: procenv-doc
BuildRequires : groff
BuildRequires : libcap-dev
BuildRequires : numactl-dev
BuildRequires : pkgconfig(check)

%description
This package contains a command-line tool that displays as much
detail about itself and its environment as possible. It can be
used as a test tool, to understand the type of environment a
process runs in, and for comparing system environments.

%package bin
Summary: bin components for the procenv package.
Group: Binaries

%description bin
bin components for the procenv package.


%package doc
Summary: doc components for the procenv package.
Group: Documentation

%description doc
doc components for the procenv package.


%prep
%setup -q -n procenv-0.46

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/procenv

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
