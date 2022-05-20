%define ProdName xs
Name: %{ProdName}-sci
Version: 1.2.23
Release: 1%{?dist}
Summary: Spectra reduction software
License: GPLv2
Url: http://www.chalmers.se/rss/oso-en/observations/data-reduction-software
Source0: ftp://yggdrasil.oso.chalmers.se/pub/xs/%{ProdName}-%{version}.tar.gz
Source1: xs-sci.desktop
BuildRequires: motif-devel libXpm-devel motif-pgplot-devel
Requires: motif libXpm motif-pgplot

%description
Spectra reduction software

%global debug_package %{nil}

%prep
%setup -q -n %{ProdName}-%{version}
%{__sed} -ie 's/675 Mass Ave, Cambridge, MA 02139, USA/51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA/g' COPYING

%build
cp -f Makefile.linux Makefile
%{__sed} -e 's|g95|gfortran|g' -i Makefile
make %{?_smp_mflags}
strip --strip-all xs

%install
%{__mkdir_p} %{buildroot}/%{_bindir}
%{__mkdir_p} %{buildroot}/%{_datadir}/pixmaps

desktop-file-install --vendor fedora					\
		     --dir %{buildroot}/%{_datadir}/applications	\
		     %{SOURCE1}

%{__install} -p -m 755 xs %{buildroot}/%{_bindir}/%{name}
%{__install} -p -m 644 %{ProdName}.xpm %{buildroot}/%{_datadir}/pixmaps/%{name}.xpm
%{__install} -p -m 644 msgs.xpm %{buildroot}/%{_datadir}/pixmaps/
%{__install} -p -m 644 gauss.xpm %{buildroot}/%{_datadir}/pixmaps/

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/*
%{_datadir}/pixmaps/*.xpm
%{_datadir}/applications/*.desktop

%changelog
* Thu Apr 14 2022 Nik <niktr@mail.ru> - 1.2.23-1
- Rebuilt v1.2.23 for Fedora 35. Renamig to xs-sci as xs package and binary already exists in repos

* Sun May 04 2008 Nik <niktr@mail.ru>
- Rebuilt for Fedora 10

* Wed Apr 30 2008 Nik <niktr@mail.ru>
- Initial build of v1.2.13 for Fedora 8
