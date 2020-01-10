%global pypi_name pyphen
%global pypi_oname Pyphen

%define python2 1

Name:           python-%{pypi_name}
Version:        0.9.1
Release:        2
Group:          Development/Python
Summary:        Pure Python module to hyphenate text

License:        MIT
URL:            http://pypi.python.org/pypi/%{pypi_name}
Source0:        http://pypi.python.org/packages/source/P/%{pypi_oname}/%{pypi_oname}-%{version}.tar.gz

BuildArch:      noarch
 
BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools

Requires:       %{pypi_name}

%rename python3-pyphen

%description
Pure Python module to hyphenate text

%package -n %{pypi_name}
Summary:        Pure Python module to hyphenate text 
Group:          Development/Python

%description -n %{pypi_name}
Pure Python module to hyphenate text

%if %python2
%package -n python2-%{pypi_name}
Summary:        Pure Python module to hyphenate text
Group:          Development/Python

Requires:       %{pypi_name}

BuildRequires:  pkgconfig(python2)
BuildRequires:  python2-setuptools

%description -n python2-%{pypi_name}
Pure Python module to hyphenate text
%endif

%prep
%setup -q -n %{pypi_oname}-%{version}

%autopatch -p1

%if %python2
cp -a . %{py2dir}
%endif

%build
%{__python} setup.py build

%if %python2
pushd %{py2dir}
%{__python2} setup.py build
popd
%endif

%install
%if %python2
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif

PYTHONDONTWRITEBYTECODE=1 %{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{python_sitelib}/%{pypi_name}*
%{python_sitelib}/%{pypi_oname}-%version-py?.?.egg-info

%files -n %{pypi_name}
%_datadir/%{pypi_name}

%if %python2
%files -n python2-%{pypi_name}
%{python2_sitelib}/%{pypi_name}*
%{python2_sitelib}/%{pypi_oname}-%version-py?.?.egg-info
%endif

