%global pypi_name pyphen
%global pypi_oname Pyphen

%define python3 0

Name:           python-%{pypi_name}
Version:        0.9.1
Release:        1
Group:          Development/Python
Summary:        Pure Python module to hyphenate text

License:        MIT
URL:            http://pypi.python.org/pypi/%{pypi_name}
Source0:        http://pypi.python.org/packages/source/P/%{pypi_oname}/%{pypi_oname}-%{version}.tar.gz

BuildArch:      noarch
 
BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools

Requires:       %{pypi_name}

%description
Pure Python module to hyphenate text

%package -n %{pypi_name}
Summary:        Pure Python module to hyphenate text 
Group:          Development/Python

%description -n %{pypi_name}
Pure Python module to hyphenate text

%if %python3
%package -n python3-%{pypi_name}
Summary:        Pure Python module to hyphenate text
Group:          Development/Python

Requires:       %{pypi_name}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools

%description -n python3-%{pypi_name}
Pure Python module to hyphenate text
%endif

%prep
%setup -q -n %{pypi_oname}-%{version}

%apply_patches

%if %python3
cp -a . %{py3dir}
%endif

%build
%{__python} setup.py build

%if %python3
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%if %python3
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{python_sitelib}/%{pypi_name}*
%{python_sitelib}/%{pypi_oname}-%version-py?.?.egg-info

%files -n %{pypi_name}
%_datadir/%{pypi_name}

%if %python3
%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}*
%{python3_sitelib}/%{pypi_oname}-%version-py?.?.egg-info
#%{python3_sitelib}/__pycache__/*
%endif

