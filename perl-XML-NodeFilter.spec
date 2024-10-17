%define upstream_name	 XML-NodeFilter
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	XML::LibXML's utility class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is a utility class used by XML::LibXML for parsing XML documents in perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/XML/*
%{_mandir}/*/*

%changelog
* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 408243
- rebuild using %%perl_convert_version

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.01-6mdv2009.0
+ Revision: 258855
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.01-5mdv2009.0
+ Revision: 246774
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.01-3mdv2008.1
+ Revision: 136367
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.01-3mdv2008.0
+ Revision: 23511
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.01-2mdk
- Fix According to perl Policy
	- Source URL
- use mkrel

* Mon Aug 30 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.01-1mdk
- Initial MDK release, needed by perl-XML-XUpdate-LibXML.

