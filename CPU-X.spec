Summary:	Gathers information on CPU, motherboard and more
Name:		CPU-X
Version:	3.2.3
Release:	1
License:	GPL v3
Group:		Applications
Source0:	https://github.com/X0rg/CPU-X/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a680ad9004e48d3c8caa758215d8269b
URL:		https://x0rg.github.io/CPU-X/
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	gtk+3-devel >= 3.12.0
BuildRequires:	libcpuid >= 0.4.0
BuildRequires:	nasm
BuildRequires:	ncurses-devel
BuildRequires:	pciutils-devel
BuildRequires:	procps-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout_c	-Werror=format-security

%description
CPU-X is a Free software that gathers information on CPU, motherboard
and more. CPU-X is similar to CPU-Z (Windows), but CPU-X is a Free and
Open Source software designed for GNU/Linux.

%prep
%setup -q

%build
mkdir -p build
cd build

%{cmake} \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/384x384

%{__mv} $RPM_BUILD_ROOT%{_localedir}/cs{_CZ,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/zh{,_CN}

%find_lang cpu-x

%clean
rm -rf $RPM_BUILD_ROOT

%files -f cpu-x.lang
%defattr(644,root,root,755)
%doc ChangeLog README.md
%attr(755,root,root) %{_bindir}/cpu-x
%attr(755,root,root) %{_bindir}/cpu-x_polkit
%{_datadir}/cpu-x
%{_desktopdir}/cpu-x-root.desktop
%{_desktopdir}/cpu-x.desktop
%{_iconsdir}/hicolor/*x*/apps/cpu-x.png
%{_datadir}/metainfo/cpu-x.appdata.xml
%{_datadir}/polkit-1/actions/org.pkexec.cpu-x.policy
