%define module  HTML-Scrubber
%define name	perl-%{module}
%define version 0.08
%define release %mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Perl extension for scrubbing/sanitizing html 
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/HTML/%{module}-%{version}.tar.bz2
BuildRequires:  perl-HTML-Parser
BuildArch:      noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
If you wanna "scrub" or "sanitize" html input in a reliable and flexible 
fashion, then this perl module is for you.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/HTML
%{_mandir}/man3/*
