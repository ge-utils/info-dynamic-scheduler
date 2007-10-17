%define topdir %(pwd)/rpmbuild
%define _topdir %{topdir} 
Summary: The SGE information plugin to gLite middleware 
Name: glite-info-dynamic-sge
Version: x
Vendor: EGEE
Release: x
License: EGEE
Group: EGEE
Source: %{name}.src.tgz
BuildArch: noarch
Prefix: /opt
Requires: perl-XML-Simple >= 2.14
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Packager: EGEE

%description
This package contains the information plugin to gLite middleware

%prep

%setup -c

%build
make install prefix=%{buildroot}%{prefix}

%files
%defattr(0644,root,root)
%{prefix}/lcg/libexec/lcg-info-dynamic-sge


%clean
rm -rf %{buildroot}
