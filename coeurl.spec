Name: coeurl
Version: 0.2.0
Release: 1
License: MIT
URL: https://nheko.im/nheko-reborn/coeurl
Summary: Simple async wrapper around CURL for C++	
Source0: https://nheko.im/nheko-reborn/coeurl/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires: meson
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libevent)	
BuildRequires: pkgconfig(spdlog)
	
%description
Simple library to do http requests asynchronously via CURL in C++.
Based on the CURL-libevent example.
	
	
%package devel	
Summary: Development files for %{name}
	
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
	
%description devel
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
	
%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_libdir}/lib%{name}.so.0*
	
%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/	
%{_libdir}/pkgconfig/%{name}.pc
	
