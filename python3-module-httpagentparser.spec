%define pypi_name httpagentparser

%def_without check

Name:    python3-module-%pypi_name
Version: 1.9.5
Release: alt1

Summary: Extracts OS Browser etc information from http user agent string
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/httpagentparser/

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst LICENSE.txt
%python3_sitelibdir/httpagentparser/
%python3_sitelibdir/httpagentparser-%version.dist-info/


%changelog
* Wed Oct 24 2023 Danilkin Danila <danild@altlinux.org> 1.9.5-alt1
- Initial build for Sisyphus
