%define name 	simplecdrx
%define version	1.3.2
%define release	%mkrel 3

Summary: 	A powerful CD creation and audio maniplation program
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Archiving/Cd burning
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0: 	%{name}-%{version}.tar.bz2
Source1:   	%{name}-16x16.png.bz2
Source2:   	%{name}-32x32.png.bz2
Source3:   	%{name}-48x48.png.bz2
Patch0:		simplecdrx-1.3.2-compile.patch.bz2
Url: 		http://ogre.rocky-road.net/cdr.shtml
BuildRequires:	gtk-devel
BuildRequires:  X11-devel
BuildRequires:  libvorbis-devel

%description
The primary goal of SimpleCDR-X is to be a powerful CD creation and audio
manipulation program.
Ease of use, flexibility, and a clean interface are of utmost importance.
SimpleCDR-X achieves this by not having the option to enable every single
mkisofs and cdrecord option. Instead a small selection of commonly
used options are available. In no way does this compromise the
power of SimpleCDR-X because a majority of the options you will
never use or know about unless you have the man page printed out for
quick reference.

%prep 
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .compile

%build
%configure
%make

%install
 [ -n "${RPM_BUILD_ROOT}" -a "${RPM_BUILD_ROOT}" != / ] \
 && rm -rf ${RPM_BUILD_ROOT}/
%makeinstall

# Mandrake Menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Categories=AudioVideo;DiscBurning;
Name=SimpleCDR-X
Comment=SimpleCDR-X
Exec=%{_bindir}/simplecdrx
Icon=%{name}
EOF

mkdir -p $RPM_BUILD_ROOT%{_miconsdir} $RPM_BUILD_ROOT%{_liconsdir} $RPM_BUILD_ROOT%{_iconsdir}
bzcat %{SOURCE1} > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
bzcat %{SOURCE2} > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
bzcat %{SOURCE3} > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post 
%{update_menus}

%postun 
%{clean_menus}

%clean
 [ -n "${RPM_BUILD_ROOT}" -a "${RPM_BUILD_ROOT}" != / ] \
 && rm -rf ${RPM_BUILD_ROOT}/
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%files 
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/*/simplecdrx*
%doc AUTHORS COPYING ChangeLog INSTALL README
%{_iconsdir}/%{name}.*
%{_miconsdir}/%{name}.*
%{_liconsdir}/%{name}.*
%{_datadir}/applications/mandriva-*.desktop
%_datadir/GETTEXT/pixmaps/*
#%{_datadir}/SimpleCDR-X/pixmaps/*

