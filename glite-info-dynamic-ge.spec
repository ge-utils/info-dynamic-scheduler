%define topdir %(pwd)/rpmbuild
%define _topdir %{topdir} 
Summary: Grid Engine info-provider.
Name: glite-info-dynamic-ge
Version: 7.0.0
Vendor: CREAM GE utils <ge-support@listas.cesga.es>
Release: 1.%{?dist}
License: Apache Software License
Group: System/Information
Source: %{name}.src.tgz
BuildArch: noarch
Requires: perl-XML-Twig >= 3.0
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Packager: Pablo Orviz <orviz@ifca.unican.es>
URL: https://github.com/ge-utils/info-dynamic-scheduler

%description
Grid Engine info-provider.

%prep

%setup -c

%build
make install prefix=%{buildroot}

%files
%defattr(0755,root,root)
%config(noreplace) /usr/libexec
%config(noreplace) /usr/libexec/glite-info-dynamic-sge
%defattr(0755,root,root)
%config(noreplace) /etc/lrms

%clean
rm -rf %{buildroot}

%changelog
* Thu May 30 2013 - Pablo Orviz <orviz@ifca.unican.es>
- Handle /etc/lrms directory creation (GGUS #94312).
