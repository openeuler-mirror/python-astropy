%global _empty_manifest_terminate_build 0
Name:		python-astropy
Version:	4.0.1.post1
Release:	1
Summary:	Community-developed python astronomy tools
License:	BSD 3-Clause License
URL:		http://astropy.org
Source0:	https://files.pythonhosted.org/packages/72/b2/18d48f5ed8dedc37e30bdf6f84ba3dc656c31dd7de9f4b6e0a2d9810cd37/astropy-4.0.1.post1.tar.gz


%description
Community-developed python astronomy tools

%package -n python3-astropy
Summary:	Community-developed python astronomy tools
Provides:	python-astropy
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-cffi
BuildRequires:	gcc
BuildRequires:	gdb
%description -n python3-astropy
Community-developed python astronomy tools

%package help
Summary:	Development documents and examples for astropy
Provides:	python3-astropy-doc
%description help
Community-developed python astronomy tools

%prep
%autosetup -n astropy-4.0.1.post1

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-astropy -f filelist.lst
%dir %{python3_sitearch}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Thu Jul 16 2020 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
