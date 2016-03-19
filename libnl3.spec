%define	api 3
%define	major 200
%define	libname %mklibname nl %{api} %{major}
%define libcli %mklibname nl-cli %{api} %{major}
%define libgenl %mklibname nl-genl %{api} %{major}
%define libnf %mklibname nl-nf %{api} %{major}
%define libroute %mklibname nl-route %{api} %{major}
%define libidiag %mklibname nl-idiag %{api} %{major}
%define libxfrm %mklibname nl-xfrm %{api} %{major}
%define	devname %mklibname -d nl %{api}

Summary:	Library for applications dealing with netlink sockets
Name:		libnl3
Version:	3.2.26
Release:	2
License:	LGPLv2
Group:		System/Libraries
Url:		https://github.com/thom311/libnl
Source0:	https://github.com/thom311/libnl/releases/download/libnl3_2_26/libnl-%{version}.tar.gz
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

%package -n %{libidiag}
Summary:	Shared library for %{name}

%description -n %{libidiag}
Netlink Inet Diag Family Library.

%package -n %{libxfrm}
Summary:	Shared library for %{name}

%description -n %{libxfrm}
Netlink Inet Diag Family Library.

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
autoreconf -fi

%build
%configure \
	--disable-static
%make

%install
%makeinstall_std

%files -n libnl3-tools
%dir %{_sysconfdir}/libnl
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/libnl/classid
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/libnl/pktloc
%{_bindir}/nl-*
%{_bindir}/nf-*
%{_bindir}/genl-ctrl-list
%{_bindir}/idiag-socket-details
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
%{_libdir}/libnl/cli/qdisc/fq_codel.so
%{_libdir}/libnl/cli/qdisc/ingress.so
%{_libdir}/libnl/cli/qdisc/hfsc.so

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

%files -n %{libidiag}
%{_libdir}/libnl-idiag-%{api}.so.%{major}*

%files -n %{libxfrm}
%{_libdir}/libnl-xfrm-%{api}.so.%{major}*

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
%dir %{_includedir}/libnl3/netlink/idiag
%dir %{_includedir}/libnl3/netlink/xfrm
%dir %{_includedir}/libnl3/netlink/route/act
%{_includedir}/libnl3/netlink/*.h
%{_includedir}/libnl3/netlink/xfrm/*.h
%{_includedir}//libnl3/netlink/idiag/*.h
%{_includedir}/libnl3/netlink/fib_lookup/*.h
%{_includedir}/libnl3/netlink/route/*.h
%{_includedir}/libnl3/netlink/route/qdisc/*.h
%{_includedir}/libnl3/netlink/route/link/*.h
%{_includedir}/libnl3/netlink/route/cls/*.h
%{_includedir}/libnl3/netlink/route/act/*.h
%{_includedir}/libnl3/netlink/route/cls/ematch/*.h
%{_includedir}/libnl3/netlink/genl/*.h
%{_includedir}/libnl3/netlink/netfilter/*.h
%{_includedir}/libnl3/netlink/cli/*.h
%{_libdir}/libnl-cli-%{api}.so
%{_libdir}/libnl-genl-%{api}.so
%{_libdir}/libnl-%{api}.so
%{_libdir}/libnl-nf-%{api}.so
%{_libdir}/libnl-route-%{api}.so
%{_libdir}/libnl-idiag-%{api}.so
%{_libdir}/libnl-xfrm-%{api}.so
%{_libdir}/pkgconfig/libnl-%{api}.0.pc
%{_libdir}/pkgconfig/libnl-cli-%{api}.0.pc
%{_libdir}/pkgconfig/libnl-genl-%{api}.0.pc
%{_libdir}/pkgconfig/libnl-nf-%{api}.0.pc
%{_libdir}/pkgconfig/libnl-route-%{api}.0.pc
%{_libdir}/pkgconfig/libnl-idiag-%{api}.0.pc
%{_libdir}/pkgconfig/libnl-xfrm-%{api}.0.pc

