%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          tkdnd
Summary:       Tk extension that adds native drag & drop capabilities
Version:       2.8
Release:       1
License:       BSD
Group:         Development/Libraries/Tcl
Source:        https://sourceforge.net/projects/tkdnd/files/TkDND/TkDND%202.8/tkdnd2.8-src.tar.gz
URL:           https://sourceforge.net/projects/tkdnd/
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel >= 8.4
BuildRequires: tk-devel >= 8.4
Requires:      tcl >= 8.4
Requires:      tk >= 8.4
BuildRoot:     %{buildroot}

%description
Tk Drag & Drop: tkdnd is an extension that adds native drag & drop capabilities
to the tk toolkit. It can be used with any tk version equal or greater to 8.4.
Under Unix the drag & drop protocol in use is the XDND protocol version 4
(also used by the QT toolkit, KDE & GNOME Desktops).

%prep
%setup -q -n %{name}%{version}

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
make DESTDIR=%{buildroot} pkglibdir=%{directory}/%{_lib}/tcl/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%doc doc/tkDND.htm license.terms
%defattr(-,root,root)
%{directory}/%{_lib}/tcl
%{directory}/share/man/mann

