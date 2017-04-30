#!/usr/bin/tclsh

set arch "x86_64"
set base "tkdnd2.8-src"

set fileurl "https://sourceforge.net/projects/tkdnd/files/TkDND/TkDND%202.8/tkdnd2.8-src.tar.gz/download"

set var [list wget $fileurl -O $base.tar.gz]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tkdnd.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove source code package
file delete $base.tar.gz

