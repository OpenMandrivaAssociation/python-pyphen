Name:		python-pyphen
Version:	0.18.1
Release:	1
Summary:	Pure Python module to hyphenate text
License:	GPL-2.0-or-later
Group:		Development/Python
URL:		https://pypi.org/project/pyphen/
Source0:	pyphen-0.18.1.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(flit-core)
BuildArch:	noarch
%description
Pure Python module to hyphenate text.

%files
%{py_sitedir}/*
