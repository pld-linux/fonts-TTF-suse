Summary:	SUSE TrueType fonts
Summary(pl.UTF-8):	Fonty TrueType z dystrybucji SUSE
Name:		fonts-TTF-suse
Version:	9.2
Release:	1
License:	Other License(s)
Group:		Fonts
Source0:	ftp://ftp.suse.com/pub/suse/i386/9.2/suse/noarch/desktop-data-SuSE-9.2-3.1.noarch.rpm
# Source0-md5:	313826c9c0454a1c2e45faf79d931265
URL:		http://www.suse.com
BuildRequires:	cpio
BuildRequires:	rpm-utils
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
This package contains SUSE TrueType fonts (TTF).

%description -l pl.UTF-8
Pakiet ten zawiera fonty TrueType (TTF) z dystrybucji SUSE.

%prep
%setup -q -c -T
rpm2cpio %{SOURCE0} | cpio -dimu
mv -f usr/X11R6/lib/X11/fonts/truetype/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ttffontsdir}
install *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{_ttffontsdir}/*
