%define major 0
%define libname %mklibname coeurl
%define devname %mklibname coeurl -d

Name: coeurl
Version: 0.3.0
Release: 2
License: MIT
URL: https://nheko.im/nheko-reborn/coeurl
Summary: Simple async wrapper around CURL for C++	
Source0: https://nheko.im/nheko-reborn/coeurl/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires: meson
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libevent)	
BuildRequires: pkgconfig(spdlog)
	
%description
Simple library to do http requests asynchronously via CURL in C++.
Based on the CURL-libevent example.

%package -n %{libname}
Summary:	Simple library to do http requests asynchronously via CURL in C++.
Group:		System/Libraries
Provides:	coeurl

%description -n %{libname}
Simple library to do http requests asynchronously via CURL in C++.
Based on the CURL-libevent example.
	
%package -n %{devname}
Summary: Development files for %{name}
	
Requires:	%{libname} = %{version}-%{release}
	
%description -n %{devname}
%{summary}.
	
%prep	
%autosetup -n %{name}-v%{version} -p1
	
%build
%meson \
	-Dwerror=false \
	-Dtests=false \
	-Dexamples=false
%meson_build

%install	
%meson_install
	
%files -n %{libname}
%doc CHANGELOG.md README.md
%license LICENSE
%{_libdir}/lib%{name}.so.*%{major}*
	
%files -n %{devname}
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/	
%{_libdir}/pkgconfig/%{name}.pc
