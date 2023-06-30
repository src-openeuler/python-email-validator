%global _empty_manifest_terminate_build 0
Name:		python-email-validator
Version:	1.3.1
Release:	1
Summary:	A robust email address syntax and deliverability validation library.
License:	CC0 (copyright waived)
URL:		https://github.com/JoshData/python-email-validator
Source0:	https://files.pythonhosted.org/packages/8e/db/5849bad11c5e03b41c7331370a2020bc98822dd8253b1861ec70351b8e75/email_validator-1.3.1.tar.gz
BuildArch:	noarch

Requires:	python3-dnspython
Requires:	python3-idna

%description
A robust email address syntax and deliverability validation library for
Python by [Joshua Tauberer](https://joshdata.me).
This library validates that a string is of the form `name@example.com`. This is
the sort of validation you would want for an email-based login form on 
a website.
Key features:
* Checks that an email address has the correct syntax --- good for
  login forms or other uses related to identifying users.
* Gives friendly error messages when validation fails (appropriate to show
  to end users).
* (optionally) Checks deliverability: Does the domain name resolve? And you can override the default DNS resolver.
* Supports internationalized domain names and (optionally)
  internationalized local parts, but blocks unsafe characters.
* Normalizes email addresses (super important for internationalized
  addresses! see below).
The library is NOT for validation of the To: line in an email message
(e.g. `My Name <my@address.com>`), which
[flanker](https://github.com/mailgun/flanker) is more appropriate for.
And this library does NOT permit obsolete forms of email addresses, so
if you need strict validation against the email specs exactly, use
[pyIsEmail](https://github.com/michaelherold/pyIsEmail).
This library is tested with Python 3.6+ but should work in earlier versions:
[![Build Status](https://app.travis-ci.com/JoshData/python-email-validator.svg?branch=main)](https://app.travis-ci.com/JoshData/python-email-validator)

%package -n python3-email-validator
Summary:	A robust email address syntax and deliverability validation library.
Provides:	python-email-validator
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pip
%description -n python3-email-validator
A robust email address syntax and deliverability validation library for
Python by [Joshua Tauberer](https://joshdata.me).
This library validates that a string is of the form `name@example.com`. This is
the sort of validation you would want for an email-based login form on 
a website.
Key features:
* Checks that an email address has the correct syntax --- good for
  login forms or other uses related to identifying users.
* Gives friendly error messages when validation fails (appropriate to show
  to end users).
* (optionally) Checks deliverability: Does the domain name resolve? And you can override the default DNS resolver.
* Supports internationalized domain names and (optionally)
  internationalized local parts, but blocks unsafe characters.
* Normalizes email addresses (super important for internationalized
  addresses! see below).
The library is NOT for validation of the To: line in an email message
(e.g. `My Name <my@address.com>`), which
[flanker](https://github.com/mailgun/flanker) is more appropriate for.
And this library does NOT permit obsolete forms of email addresses, so
if you need strict validation against the email specs exactly, use
[pyIsEmail](https://github.com/michaelherold/pyIsEmail).
This library is tested with Python 3.6+ but should work in earlier versions:
[![Build Status](https://app.travis-ci.com/JoshData/python-email-validator.svg?branch=main)](https://app.travis-ci.com/JoshData/python-email-validator)

%package help
Summary:	Development documents and examples for email-validator
Provides:	python3-email-validator-doc
%description help
A robust email address syntax and deliverability validation library for
Python by [Joshua Tauberer](https://joshdata.me).
This library validates that a string is of the form `name@example.com`. This is
the sort of validation you would want for an email-based login form on 
a website.
Key features:
* Checks that an email address has the correct syntax --- good for
  login forms or other uses related to identifying users.
* Gives friendly error messages when validation fails (appropriate to show
  to end users).
* (optionally) Checks deliverability: Does the domain name resolve? And you can override the default DNS resolver.
* Supports internationalized domain names and (optionally)
  internationalized local parts, but blocks unsafe characters.
* Normalizes email addresses (super important for internationalized
  addresses! see below).
The library is NOT for validation of the To: line in an email message
(e.g. `My Name <my@address.com>`), which
[flanker](https://github.com/mailgun/flanker) is more appropriate for.
And this library does NOT permit obsolete forms of email addresses, so
if you need strict validation against the email specs exactly, use
[pyIsEmail](https://github.com/michaelherold/pyIsEmail).
This library is tested with Python 3.6+ but should work in earlier versions:
[![Build Status](https://app.travis-ci.com/JoshData/python-email-validator.svg?branch=main)](https://app.travis-ci.com/JoshData/python-email-validator)

%prep
%autosetup -n email_validator-1.3.1

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

%files -n python3-email-validator -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Sat Mar 25 2023 Python_Bot <Python_Bot@openeuler.org> - 1.3.1-1
- Package Spec generated
