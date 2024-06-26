#!/usr/bin/tclsh

set arch "x86_64"
set base "tkdnd-release-test-v2.9.4"

set fileurl "https://github.com/petasis/tkdnd/archive/refs/tags/tkdnd-release-test-v2.9.4.tar.gz"

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

