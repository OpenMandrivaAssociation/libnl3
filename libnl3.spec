%define	major 3
%define	libname %mklibname nl _%{major}
%define	develname %mklibname -d nl _%{major}

Summary:	Library for applications dealing with netlink sockets
Name:		libnl3
Version:	3.2.3
Release:	%mkrel 1
License:	LGPL
Group:		System/Libraries
URL:		http://people.suug.ch/~tgr/libnl/
Source0:	http://people.suug.ch/~tgr/libnl/files/libnl-%{version}.tar.gz
Patch0:		libnl-3.2.3-avoid-version.diff
Patch1:		libnl-3.2.3-tooooo_many_commas_fix.diff
Patch2:		libnl-3.2.3-avoid-dangling-co_major_cache-reference-to-NL_AUTO_P.diff
BuildRequires:	automake autoconf libtool
BuildRequires:	bison
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	graphviz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
libnl is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and
various netlink family specific interfaces.

%package -n	libnl3-tools
Summary:	Applications dealing with netlink sockets
Group:		System/Kernel and hardware

%description -n	libnl3-tools
libnl is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and
various netlink family specific interfaces.

%package -n	%{libname}
Summary:	Library for applications dealing with netlink sockets
Group:		System/Libraries

%description -n	%{libname}
libnl is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and
various netlink family specific interfaces.

%package -n	%{develname}
Summary:	Header files of libnl
Group:		Development/C
Requires:	%{libname} >= %{version}
Provides:	libnl3-devel = %{version}-%{release}

%description -n	%{develname}
libnl is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and
various netlink family specific interfaces.

%prep

%setup -q -n libnl-%{version}
%patch0 -p0
%patch1 -p1
%patch2 -p0

# a quick hack to make doxygen stripping builddir from html outputs.
sed -i.org -e "s,^STRIP_FROM_PATH.*,STRIP_FROM_PATH = `pwd`," doc/Doxyfile.in

%build
autoreconf -fi
%configure2_5x \
    --disable-static
%make

%install
rm -rf %{buildroot}

%makeinstall_std

# clenuo
rm -f %{buildroot}%{_libdir}/*.*a
rm -f %{buildroot}%{_libdir}/libnl/cli/qdisc/*.*a
rm -f %{buildroot}%{_libdir}/libnl/cli/cls/*.*a

%clean
rm -rf %{buildroot}

%files -n libnl3-tools
%defattr(-,root,root)
%{_sbindir}/nl-*
%{_mandir}/man8/*

%files -n %{libname}
%defattr(-,root,root)
%dir %{_sysconfdir}/libnl
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/libnl/classid
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/libnl/pktloc
%{_libdir}/libnl-cli-%{major}.so.*
%{_libdir}/libnl-genl-%{major}.so.*
%{_libdir}/libnl-%{major}.so.*
%{_libdir}/libnl-nf-%{major}.so.*
%{_libdir}/libnl-route-%{major}.so.*
%dir %{_libdir}/libnl
%dir %{_libdir}/libnl/cli
%dir %{_libdir}/libnl/cli/qdisc
%dir %{_libdir}/libnl/cli/cls
%{_libdir}/libnl/cli/qdisc/htb.so
%{_libdir}/libnl/cli/qdisc/blackhole.so
%{_libdir}/libnl/cli/qdisc/pfifo.so
%{_libdir}/libnl/cli/qdisc/bfifo.so
%{_libdir}/libnl/cli/cls/basic.so
%{_libdir}/libnl/cli/cls/cgroup.so

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/libnl3
%dir %{_includedir}/libnl3/netlink
%dir %{_includedir}/libnl3/netlink/fib_lookup
%dir %{_includedir}/libnl3/netlink/route
%dir %{_includedir}/libnl3/netlink/route/qdisc
%dir %{_includedir}/libnl3/netlink/route/link
%dir %{_includedir}/libnl3/netlink/route/cls
%dir %{_includedir}/libnl3/netlink/route/cls/ematch
%dir %{_includedir}/libnl3/netlink/genl
%dir %{_includedir}/libnl3/netlink/netfilter
%dir %{_includedir}/libnl3/netlink/cli
%{_includedir}/libnl3/netlink/*.h
%{_includedir}/libnl3/netlink/fib_lookup/*.h
%{_includedir}/libnl3/netlink/route/*.h
%{_includedir}/libnl3/netlink/route/qdisc/*.h
%{_includedir}/libnl3/netlink/route/link/*.h
%{_includedir}/libnl3/netlink/route/cls/*.h
%{_includedir}/libnl3/netlink/route/cls/ematch/*.h
%{_includedir}/libnl3/netlink/genl/*.h
%{_includedir}/libnl3/netlink/netfilter/*.h
%{_includedir}/libnl3/netlink/cli/*.h
%{_libdir}/libnl-cli-%{major}.so
%{_libdir}/libnl-genl-%{major}.so
%{_libdir}/libnl-%{major}.so
%{_libdir}/libnl-nf-%{major}.so
%{_libdir}/libnl-route-%{major}.so
%{_libdir}/pkgconfig/libnl-%{major}.0.pc
%{_libdir}/pkgconfig/libnl-cli-%{major}.0.pc
%{_libdir}/pkgconfig/libnl-genl-%{major}.0.pc
%{_libdir}/pkgconfig/libnl-nf-%{major}.0.pc
%{_libdir}/pkgconfig/libnl-route-%{major}.0.pc

