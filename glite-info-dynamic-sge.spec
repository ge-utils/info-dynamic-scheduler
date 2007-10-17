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
%{prefix}/lcg/share/docs/lcg-info-dynamic-sge/AUTHORS
%{prefix}/lcg/share/docs/lcg-info-dynamic-sge/CREDITS
%{prefix}/lcg/share/docs/lcg-info-dynamic-sge/LICENSE
%{prefix}/lcg/share/docs/lcg-info-dynamic-sge/License.GPL
%{prefix}/lcg/share/docs/lcg-info-dynamic-sge/README
%{prefix}/lcg/share/docs/lcg-info-dynamic-sge/cluster.state.template
%{prefix}/lcg/share/docs/lcg-info-dynamic-sge/info-reporter.conf.template
%{prefix}/lcg/share/docs/lcg-info-dynamic-sge/sample-vqueues.conf.template
%{prefix}/lcg/share/docs/lcg-info-dynamic-sge/compare-output

%clean
rm -rf %{buildroot}

