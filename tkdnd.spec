%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          tkdnd
Summary:       Tk extension that adds native drag & drop capabilities
Version:       2.9.4
Release:       1
License:       TCL
Group:         Development/Libraries/Tcl
Source:        tkdnd-release-test-v2.9.4.tar.gz
URL:           https://github.com/petasis/tkdnd
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel >= 8.4
BuildRequires: tk-devel >= 8.4
BuildRequires: libXcursor-devel
Requires:      tcl >= 8.4
Requires:      tk >= 8.4
BuildRoot:     %{buildroot}

%description
Tk Drag & Drop: tkdnd is an extension that adds native drag & drop capabilities
to the tk toolkit. It can be used with any tk version equal or greater to 8.4.
Under Unix the drag & drop protocol in use is the XDND protocol version 4
(also used by the QT toolkit, KDE & GNOME Desktops).

%prep
%setup -q -n %{name}-%{name}-release-test-v%{version}

%build
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib} \
%ifarch x86_64
	--enable-64bit \
%endif
	--with-tcl=%{directory}/%{_lib} \
	--with-tk=%{directory}/%{_lib}
make 

%install
make DESTDIR=%{buildroot} pkglibdir=%{tcl_archdir}/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%doc doc/tkDND.htm license.terms
%defattr(-,root,root)
%{tcl_archdir}
%{directory}/share/man/mann

