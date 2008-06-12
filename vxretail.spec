Summary:	BananaPOS Point Of Sale Terminal
Name:		vxretail
Version:	2.0.0
Release:	%mkrel 0.beta3.2
License:	GPL
Group:		Databases
URL:		http://www.bananahead.com
Source0:	http://www.bananahead.com/download/bhpos/stable/%{name}-%{version}.tar.bz2
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:	gtkmm2.4
BuildRequires:	gtkmm2.4-devel
BuildRequires:	ImageMagick
BuildRequires:	intltool
BuildRequires:	libgtk+2-devel >= 2.6
BuildRequires:	libsigc++2.0-devel >= 2.0
BuildRequires:	libtool >= 1.5
BuildRequires:	libusb-devel >= 0.1.8
BuildRequires:	libxml2 >= 2.5.8
BuildRequires:	libxml++-devel >= 2.6
BuildRequires:	MySQL-devel
BuildRequires:	pkgconfig
BuildRequires:	bhpos_base >= 2.0.0
BuildRequires:	bhpos_base-devel >= 2.0.0
BuildRequires:	libbhpos_commonlibs-devel >= 2.0.0
BuildRequires:	libbhpos_hwlib-devel >= 2.0.0
BuildRequires:	libbhpos_mflibs-devel >= 2.0.0
BuildRequires:	libbhpos_mfposengine-devel >= 2.0.0
BuildRequires:	gettext-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
BananaPOS Point Of Sale Terminal.

%prep

%setup -q -n %{name}-%{version}

%build
sh ./autogen.sh

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

# Mandriva Icons
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_miconsdir}
install -d %{buildroot}%{_liconsdir}
convert share/images/splash.png -geometry 48x48 %{buildroot}%{_liconsdir}/%{name}.png
convert share/images/splash.png -geometry 32x32 %{buildroot}%{_iconsdir}/%{name}.png
convert share/images/splash.png -geometry 16x16 %{buildroot}%{_miconsdir}/%{name}.png

# Mandriva Menus

# XDG menu
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=BananaPOS Point Of Sale Terminal
Exec=%{_sbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Finances;
EOF

%if %mdkversion < 200900
%post
%update_menus
%update_desktop_database
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_desktop_database
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/vxpos/vxretail-lite.conf
%{_bindir}/vxretail
%{_datadir}/bhpos2.0/images/*.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop


