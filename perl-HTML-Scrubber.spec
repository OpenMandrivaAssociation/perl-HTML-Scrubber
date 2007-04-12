%define realname   HTML-Scrubber

Name:		perl-%{realname}
Version:    0.08
Release: %mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Perl extension for scrubbing/sanitizing html 
Source0:    http://search.cpan.org/CPAN/authors/id/P/PO/PODMASTER/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:  perl-HTML-Parser
BuildArch: noarch

%description
If you wanna "scrub" or "sanitize" html input in a reliable and flexible 
fashion, then this perl module is for you.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

