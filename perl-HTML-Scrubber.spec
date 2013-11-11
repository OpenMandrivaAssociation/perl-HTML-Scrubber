%define upstream_name    HTML-Scrubber
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Perl extension for scrubbing/sanitizing html 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/HTML-Scrubber-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Parser)
BuildArch:	noarch

%description
If you wanna "scrub" or "sanitize" html input in a reliable and flexible 
fashion, then this perl module is for you.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes README
%{perl_vendorlib}/HTML
%{_mandir}/man3/*

%changelog
* Mon Apr 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 650310
- update to new version 0.09

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 406062
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.08-7mdv2009.0
+ Revision: 241477
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Sep 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-5mdv2008.0
+ Revision: 78778
- spec cleanup

* Thu Jun 21 2007 Michael Scherer <misc@mandriva.org> 0.08-4mdv2008.0
+ Revision: 41990
- rebuild


* Wed Dec 28 2005 Michael Scherer <misc@mandriva.org> 0.08-3mdk
- Do not ship empty dir

* Mon Oct 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.08-2mdk
- Fix BuildRequires

* Sat Oct 01 2005 Michael Scherer <misc@mandriva.org> 0.08-1mdk
- First mandriva package


