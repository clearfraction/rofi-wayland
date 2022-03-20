Name     : rofi-wayland
Version  : 1.7.3
Release  : 3
URL      : https://github.com/lbonn/rofi/
Source0  : https://github.com/lbonn/rofi/releases/download/1.7.3%2Bwayland1/rofi-%{version}+wayland1.tar.xz
Summary  : Header files for rofi plugins
Group    : Development/Tools
License  : MIT
Requires: rofi-wayland-bin = %{version}-%{release}
Requires: rofi-wayland-data = %{version}-%{release}
Requires: rofi-wayland-license = %{version}-%{release}
Requires: rofi-wayland-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-meson
BuildRequires : flex
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-xcb)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libstartup-notification-1.0)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(xcb-xrm)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : wayland-dev wayland-protocols-dev
BuildRequires : xcb-util-cursor-dev
BuildRequires : cmake



%description
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ca0310962a7c4b829d0c57f1ab023531)](https://app.codacy.com/app/davatorium/rofi?utm_source=github.com&utm_medium=referral&utm_content=davatorium/rofi&utm_campaign=Badge_Grade_Settings)
[![Build Status](https://travis-ci.org/davatorium/rofi.svg?branch=master)](https://travis-ci.org/davatorium/rofi)
[![codecov.io](https://codecov.io/github/davatorium/rofi/coverage.svg?branch=master)](https://codecov.io/github/davatorium/rofi?branch=master)
[![Issues](https://img.shields.io/github/issues/davatorium/rofi.svg)](https://github.com/davatorium/rofi/issues)
[![Forks](https://img.shields.io/github/forks/davatorium/rofi.svg)](https://github.com/davatorium/rofi/network)
[![Stars](https://img.shields.io/github/stars/davatorium/rofi.svg)](https://github.com/davatorium/rofi/stargazers)
[![Downloads](https://img.shields.io/github/downloads/davatorium/rofi/total.svg)](https://github.com/davatorium/rofi/releases)
[![Coverity](https://scan.coverity.com/projects/3850/badge.svg)](https://scan.coverity.com/projects/davedavenport-rofi)
[![Forum](https://img.shields.io/badge/forum-online-green.svg)](https://reddit.com/r/qtools/)

%package bin
Summary: bin components for the rofi package.
Group: Binaries
Requires: rofi-wayland-data = %{version}-%{release}
Requires: rofi-wayland-license = %{version}-%{release}

%description bin
bin components for the rofi package.


%package data
Summary: data components for the rofi package.
Group: Data

%description data
data components for the rofi package.


%package dev
Summary: dev components for the rofi package.
Group: Development
Requires: rofi-wayland-bin = %{version}-%{release}
Requires: rofi-wayland-data = %{version}-%{release}
Provides: rofi-wayland-devel = %{version}-%{release}
Requires: rofi = %{version}-%{release}

%description dev
dev components for the rofi package.


%package license
Summary: license components for the rofi package.
Group: Default

%description license
license components for the rofi package.


%package man
Summary: man components for the rofi package.
Group: Default

%description man
man components for the rofi package.


%prep
%setup -q -n rofi-%{version}+wayland1
cd %{_builddir}/rofi-%{version}+wayland1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605557300
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
meson \
    --libdir=lib64 --prefix=/usr \
    --buildtype=plain builddir
ninja -v -C builddir

%install
export SOURCE_DATE_EPOCH=1605557300
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rofi
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rofi
/usr/bin/rofi-sensible-terminal
/usr/bin/rofi-theme-selector

%files data
%defattr(-,root,root,-)
/usr/share/rofi/themes/Adapta-Nokto.rasi
/usr/share/rofi/themes/Arc-Dark.rasi
/usr/share/rofi/themes/Arc.rasi
/usr/share/rofi/themes/DarkBlue.rasi
/usr/share/rofi/themes/Indego.rasi
/usr/share/rofi/themes/Monokai.rasi
/usr/share/rofi/themes/Paper.rasi
/usr/share/rofi/themes/Pop-Dark.rasi
/usr/share/rofi/themes/android_notification.rasi
/usr/share/rofi/themes/arthur.rasi
/usr/share/rofi/themes/blue.rasi
/usr/share/rofi/themes/c64.rasi
/usr/share/rofi/themes/dmenu.rasi
/usr/share/rofi/themes/fancy.rasi
/usr/share/rofi/themes/glue_pro_blue.rasi
/usr/share/rofi/themes/gruvbox-common.rasi
/usr/share/rofi/themes/gruvbox-dark-hard.rasi
/usr/share/rofi/themes/gruvbox-dark-soft.rasi
/usr/share/rofi/themes/gruvbox-dark.rasi
/usr/share/rofi/themes/gruvbox-light-hard.rasi
/usr/share/rofi/themes/gruvbox-light-soft.rasi
/usr/share/rofi/themes/gruvbox-light.rasi
/usr/share/rofi/themes/lb.rasi
/usr/share/rofi/themes/paper-float.rasi
/usr/share/rofi/themes/purple.rasi
/usr/share/rofi/themes/sidebar.rasi
/usr/share/rofi/themes/solarized.rasi
/usr/share/rofi/themes/solarized_alternate.rasi

%files dev
%defattr(-,root,root,-)
/usr/include/rofi/helper.h
/usr/include/rofi/mode-private.h
/usr/include/rofi/mode.h
/usr/include/rofi/rofi-icon-fetcher.h
/usr/include/rofi/rofi-types.h
/usr/lib64/pkgconfig/rofi.pc

%files license
%defattr(0644,root,root,0755)

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/rofi-sensible-terminal.1
/usr/share/man/man1/rofi-theme-selector.1
/usr/share/man/man1/rofi.1
/usr/share/man/man5/rofi-theme.5
/usr/share/man/man5/rofi-dmenu.5
/usr/share/man/man5/rofi-keys.5
/usr/share/man/man5/rofi-script.5
/usr/share/rofi/themes/docu.rasi
/usr/share/rofi/themes/iggy.jpg
/usr/share/rofi/themes/iggy.rasi


# forked from https://github.com/clearlinux-pkgs/rofi/
