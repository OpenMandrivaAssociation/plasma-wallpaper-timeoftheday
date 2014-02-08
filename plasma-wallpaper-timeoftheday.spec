Name: plasma-wallpaper-timeoftheday
Summary: A Plasma Wallpaper that changes wallpaper based on day hour
Version: 0.1
Release: 9
Source0: plasma-wallpaper-timeoftheday-%{version}.tar.bz2
Patch0:  plasma-wallpaper-timeoftheday-0.1-add-translation.patch
Patch1:  plasma-wallpaper-timeoftheday-0.1-remove-debug.patch
Patch2:  plasma-wallpaper-timeoftheday-0.1-less-transitions.patch
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
%patch0 -p0
%patch1 -p0
%patch2 -p0

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


%changelog
* Tue Feb 21 2012 abf
- The release updated by ABF

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-7mdv2011.0
+ Revision: 667782
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-6mdv2011.0
+ Revision: 607178
- rebuild

* Wed May 19 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1-5mdv2010.1
+ Revision: 545453
- Do less transitions, to use less CPU
  CCBUG: 59308

* Tue May 11 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1-4mdv2010.1
+ Revision: 544498
- Remove img created for debug

* Tue May 11 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1-3mdv2010.1
+ Revision: 544463
- Activate translations

* Mon Nov 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1-2mdv2010.1
+ Revision: 463838
- Rebuild against new KDE ( fixes upstream bug #213654)

* Thu Oct 29 2009 Arthur Renato Mello <arthur@mandriva.com> 0.1-1mdv2010.0
+ Revision: 460099
- import plasma-wallpaper-timeoftheday

