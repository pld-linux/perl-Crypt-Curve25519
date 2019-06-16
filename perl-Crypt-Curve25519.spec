%define		pdir	Crypt
%define		pnam	Curve25519
%include	/usr/lib/rpm/macros.perl
Summary:	Crypt::Curve25519 Perl module - Generate shared secret using elliptic-curve Diffie-Hellman function
Name:		perl-Crypt-Curve25519
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	631c7a0e799994712e3d802317615a4c
Patch0:		%{name}-fmul.patch
URL:		http://search.cpan.org/dist/Crypt-Curve25519/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.56
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Curve25519 is a state-of-the-art Diffie-Hellman function suitable for
a wide variety of applications.

Given a user's 32-byte secret key, Curve25519 computes the user's
32-byte public key. Given the user's 32-byte secret key and another
user's 32-byte public key, Curve25519 computes a 32-byte secret shared
by the two users. This secret can then be used to authenticate and
encrypt messages between the two users.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/auto/Crypt/Curve25519
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Curve25519/Curve25519.so
%{perl_vendorarch}/Crypt/Curve25519.pm
%{_mandir}/man3/*
