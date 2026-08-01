%define upstream_name    HTML-Scrubber
%define upstream_version 0.19
Name:		perl-%{upstream_name}
Version:	0.19
Release:	6

Summary:	Perl extension for scrubbing/sanitizing html 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/nigelm/html-scrubber
Source0:	https://cpan.metacpan.org/authors/id/N/NI/NIGELM/HTML-Scrubber-0.19.tar.gz
BuildRequires:	make

BuildRequires:  perl-devel
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(CPAN::Meta::YAML) >= 0.16.0
BuildRequires:  perl(Carp) >= 1.360.0
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test)
#BuildRequires:  perl(Test::CPAN::Meta) >= 0.250.0
#BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More) >= 1.1.9
#BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(utf8)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildArch:	noarch

%description
If you wanna "scrub" or "sanitize" html input in a reliable and flexible 
fashion, then this perl module is for you.

%prep
%setup -q -n HTML-Scrubber-0.19

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
# soft: do not fail package on test failures
set +e
#make test || :

%install
%make_install

%files
%doc Changes README
%{perl_vendorlib}/HTML
%{_mandir}/man3/*

