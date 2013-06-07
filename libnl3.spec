%define	api	3
%define	major	200
%define	libname %mklibname nl %{api} %{major}
%define libcli	%mklibname nl-cli %{api} %{major}
%define libgenl	%mklibname nl-genl %{api} %{major}
%define libnf	%mklibname nl-nf %{api} %{major}
%define libroute %mklibname nl-route %{api} %{major}
%define	devname %mklibname -d nl %{api}

Summary:	Library for applications dealing with netlink sockets
Name:		libnl3
Version:	3.2.22
Release:	2
License:	LGPLv2
Group:		System/Libraries
Url:		http://www.carisma.slowglass.com/~tgr/libnl/
Source0:	http://www.carisma.slowglass.com/~tgr/libnl/files/libnl-%{version}.tar.gz
Patch0:		libnl-3.2.3-tooooo_many_commas_fix.diff
BuildRequires:	bison
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	graphviz
BuildRequires:	libtool

%track
prog %{name} = {
	url = http://www.carisma.slowglass.com/~tgr/libnl/
	regex = "Version (__VER__) has been released"
	version = %{version}
}

%description
libnl is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and
various netlink family specific interfaces.

%package -n	libnl3-tools
Summary:	Applications dealing with netlink sockets
Group:		System/Kernel and hardware
Conflicts:	%{_lib}nl_3 < 3.2.22-2

%description -n	libnl3-tools
libnl is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and
various netlink family specific interfaces.

%package -n	%{libname}
Summary:	Library for applications dealing with netlink sockets
Group:		System/Libraries
Obsoletes:	%{_lib}nl_3 < 3.2.22-2
Conflicts:	%{_lib}nl_3 < 3.2.22-2

%description -n	%{libname}
This package contains a shared library for %{name}.

%package -n	%{libcli}
Summary:	Library for applications dealing with netlink sockets
Group:		System/Libraries
Conflicts:	%{_lib}nl_3 < 3.2.22-2

%description -n	%{libcli}
This package contains a shared library for %{name}.

%package -n	%{libgenl}
Summary:	Library for applications dealing with netlink sockets
Group:		System/Libraries
Conflicts:	%{_lib}nl_3 < 3.2.22-2

%description -n	%{libgenl}
This package contains a shared library for %{name}.

%package -n	%{libnf}
Summary:	Library for applications dealing with netlink sockets
Group:		System/Libraries
Conflicts:	%{_lib}nl_3 < 3.2.22-2

%description -n	%{libnf}
This package contains a shared library for %{name}.

%package -n	%{libroute}
Summary:	Library for applications dealing with netlink sockets
Group:		System/Libraries
Conflicts:	%{_lib}nl_3 < 3.2.22-2

%description -n	%{libroute}
This package contains a shared library for %{name}.

%package -n	%{devname}
Summary:	Header files of libnl
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{libcli} = %{version}-%{release}
Requires:	%{libgenl} = %{version}-%{release}
Requires:	%{libnf} = %{version}-%{release}
Requires:	%{libroute} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
libnl is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and
various netlink family specific interfaces.

%prep
%setup -qn libnl-%{version}
#patch0 -p1

# a quick hack to make doxygen stripping builddir from html outputs.
#sed -i.org -e "s,^STRIP_FROM_PATH.*,STRIP_FROM_PATH = `pwd`," doc/Doxyfile.in
autoreconf -fi

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

# clenuo
#rm -f %{buildroot}%{_libdir}/*.la
#rm -f %{buildroot}%{_libdir}/libnl/cli/qdisc/*.*a
#rm -f %{buildroot}%{_libdir}/libnl/cli/cls/*.*a

%files -n libnl3-tools
%dir %{_sysconfdir}/libnl
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/libnl/classid
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/libnl/pktloc
%{_sbindir}/nl-*
%{_sbindir}/genl-ctrl-list
%{_mandir}/man8/*
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
%{_libdir}/libnl/cli/qdisc/plug.so

%files -n %{libname}
%{_libdir}/libnl-%{api}.so.%{major}*

%files -n %{libcli}
%{_libdir}/libnl-cli-%{api}.so.%{major}*

%files -n %{libgenl}
%{_libdir}/libnl-genl-%{api}.so.%{major}*

%files -n %{libnf}
%{_libdir}/libnl-nf-%{api}.so.%{major}*

%files -n %{libroute}
%{_libdir}/libnl-route-%{api}.so.%{major}*

%files -n %{devname}
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
%{_libdir}/libnl-cli-%{api}.so
%{_libdir}/libnl-genl-%{api}.so
%{_libdir}/libnl-%{api}.so
%{_libdir}/libnl-nf-%{api}.so
%{_libdir}/libnl-route-%{api}.so
%{_libdir}/pkgconfig/libnl-%{api}.0.pc
%{_libdir}/pkgconfig/libnl-cli-%{api}.0.pc
%{_libdir}/pkgconfig/libnl-genl-%{api}.0.pc
%{_libdir}/pkgconfig/libnl-nf-%{api}.0.pc
%{_libdir}/pkgconfig/libnl-route-%{api}.0.pc

