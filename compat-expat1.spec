Summary: A library for parsing XML documents
Name: compat-expat1
Version: 1.95.8
Release: 8%{?dist}
Group: System Environment/Libraries
Source: http://downloads.sourceforge.net/expat/expat-%{version}.tar.gz
Patch1: expat-2.0.1-CVE-2009-3560-revised.patch
Patch2: expat-1.95.8-CVE-2009-3720.patch
URL: http://www.libexpat.org/
License: MIT
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: autoconf, automake, libtool

%description
This is expat, the C library for parsing XML, written by James Clark. Expat
is a stream oriented XML parser. This means that you register handlers with
the parser prior to starting the parse. These handlers are called when the
parser discovers the associated structures in the document being parsed. A
start tag is an example of the kind of structures for which you may
register handlers.

%prep
%setup -q -n expat-%{version}
%patch1 -p1 -b .cve3560
%patch2 -p1 -b .cve3720

%build
rm -rf autom4te*.cache
cp `aclocal --print-ac-dir`/libtool.m4 conftools || exit 1
libtoolize --copy --force --automake && aclocal && autoheader && autoconf
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}

%makeinstall man1dir=$RPM_BUILD_ROOT/%{_mandir}/man1 

rm -rf $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_datadir}/man} \
       $RPM_BUILD_ROOT%{_libdir}/libexpat.{a,la,so}

%clean
rm -rf ${RPM_BUILD_ROOT}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/lib*.so.*

%changelog
* Mon Feb 15 2010 Joe Orton <jorton@redhat.com> - 1.95.8-8
- fix regressions in CVE-2009-3560

* Tue Jan 19 2010 Joe Orton <jorton@redhat.com> - 1.95.8-7
- add security fixes for CVE-2009-3560 CVE-2009-3720 (#556778)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.95.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.95.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.95.8-4
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Joe Orton <jorton@redhat.com> 1.95.8-3
- fix Source location

* Wed Aug  8 2007 Joe Orton <jorton@redhat.com> 1.95.8-2
- fix License tag

* Thu Jul 26 2007 Joe Orton <jorton@redhat.com> 1.95.8-1
- new package
