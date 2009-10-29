Name: plasma-wallpaper-timeoftheday
Summary: A Plasma Wallpaper that changes wallpaper based on day hour
Version: 0.1
Release: %mkrel 1
Source0: plasma-wallpaper-timeoftheday-%{version}.tar.bz2
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPL
BuildRequires: qt4-devel
BuildRequires: kde4-macros
BuildRequires: kdelibs4-devel
BuildRequires: kdebase4-workspace-devel
BuildRequires: cmake

%description
A Plasma Wallpaper that changes wallpaper based on day hour

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_wallpaper_timeoftheday.so
%_kde_services/plasma-wallpaper-timeoftheday.desktop
