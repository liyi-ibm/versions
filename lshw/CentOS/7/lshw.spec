# Conditional build (--with/--without option)
#   --without gui

Summary: HardWare LiSter
Name: lshw
Version: B.02.18.77
Release: 2
#Source: http://www.ezix.org/software/files/%{name}-%{version}.tar.gz
URL: http://lshw.ezix.org/
License: GPL
Group: Applications/System
#BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:        %{name}.tar.gz

%define _without_gui 1 

%description
lshw (Hardware Lister) is a small tool to provide detailed informaton on
the hardware configuration of the machine. It can report exact memory
configuration, firmware version, mainboard configuration, CPU version
and speed, cache configuration, bus speed, etc. on DMI-capable x86s
systems and on some PowerPC machines (PowerMac G4 is known to work).

Information can be output in plain text, XML or HTML.

For detailed information on lshw features and usage, please see the
included documentation or go to the lshw Web page,
http://lshw.ezix.org/

%if %{!?_without_gui:1}0
%package gui
Summary: HardWare LiSter (GUI version)
Group: Applications/System
Requires: %{name} >= %{version}
Requires: gtk2 >= 2.4
BuildRequires: gtk2-devel >= 2.4

%description gui
lshw (Hardware Lister) is a small tool to provide detailed informaton on
the hardware configuration of the machine. It can report exact memory
configuration, firmware version, mainboard configuration, CPU version
and speed, cache configuration, bus speed, etc. on DMI-capable x86s
 systems and on some PowerPC machines (PowerMac G4 is known to work).

This package provides a graphical user interface to display hardware
information.

For detailed information on lshw features and usage, please see the
included documentation or go to the lshw Web page,
http://lshw.ezix.org/

%endif

%prep
%setup -q -n %{name}

%build
%{__make} %{?_smp_mflags} \
  PREFIX="%{_prefix}" \
  SBINDIR="%{_sbindir}" \
  MANDIR="%{_mandir}" \
  DATADIR="%{_datadir}" \
  all
%if %{!?_without_gui:1}0
%{__make} %{?_smp_mflags} \
  PREFIX="%{_prefix}" \
  SBINDIR="%{_sbindir}" \
  MANDIR="%{_mandir}" \
  DATADIR="%{_datadir}" \
  gui
%endif

%install
%{__rm} -rf "%{buildroot}"

%{__make} \
  DESTDIR="%{buildroot}" \
  PREFIX="%{_prefix}" \
  SBINDIR="%{_sbindir}" \
  MANDIR="%{_mandir}" \
  DATADIR="%{_datadir}" \
  INSTALL="%{__install} -p" \
  install
%if %{!?_without_gui:1}0
%{__make} \
  DESTDIR="%{buildroot}" \
  PREFIX="%{_prefix}" \
  SBINDIR="%{_sbindir}" \
  MANDIR="%{_mandir}" \
  DATADIR="%{_datadir}" \
  INSTALL="%{__install} -p" \
  install-gui
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root, 0555)
%doc README.md COPYING docs/TODO docs/Changelog docs/lshw.xsd
%{_sbindir}/lshw
%doc %{_mandir}/man?/*
%{_datadir}/lshw/
%{_datadir}/locale/*/*/*

%if %{!?_without_gui:1}0
%files gui
%defattr(-,root,root, 0555)
%doc COPYING
%{_sbindir}/gtk-lshw
%endif

%changelog
* Tue May  1 2007 Lyonel Vincent <lyonel@ezix.org> B.02.10-2
- spec file cleanup

* Thu Apr 10 2003 Lyonel Vincent <lyonel@ezix.org> A.01.00-1
- RPM packaging
