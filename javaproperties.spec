#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : javaproperties
Version  : 0.7.0
Release  : 9
URL      : https://files.pythonhosted.org/packages/3e/60/4d55e0cf797ef01a1987f85f936ae5086f2f8d1957d84303a43b64e42a92/javaproperties-0.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/3e/60/4d55e0cf797ef01a1987f85f936ae5086f2f8d1957d84303a43b64e42a92/javaproperties-0.7.0.tar.gz
Summary  : Read & write Java .properties files
Group    : Development/Tools
License  : MIT
Requires: javaproperties-python = %{version}-%{release}
Requires: javaproperties-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: http://www.repostatus.org/badges/latest/active.svg
:target: http://www.repostatus.org/#active
:alt: Project Status: Active - The project has reached a stable, usable
state and is being actively developed.

%package python
Summary: python components for the javaproperties package.
Group: Default
Requires: javaproperties-python3 = %{version}-%{release}

%description python
python components for the javaproperties package.


%package python3
Summary: python3 components for the javaproperties package.
Group: Default
Requires: python3-core
Provides: pypi(javaproperties)
Requires: pypi(six)

%description python3
python3 components for the javaproperties package.


%prep
%setup -q -n javaproperties-0.7.0
cd %{_builddir}/javaproperties-0.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588709957
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
