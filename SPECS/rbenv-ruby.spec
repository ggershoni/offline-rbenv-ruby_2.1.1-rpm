Name:		rbenv-ruby_2.1.1
Version: 	2.1.1
Release: 	1%{?dist:%{dist}}
Group: 		Development/Languages
Summary: 	A ruby instance that can co-exist with other instances in the rbenv (RPM) ecosystem.
License: 	MIT
URL: 		https://https://github.com/ggershoni/offline-rbenv-ruby_2.1.1-rpm
Source0: 	ruby-2.1.1.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires: 	redhat-rpm-config readline libyaml libyaml-devel readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make libffi-devel
Requires: 	libyaml

%description
Installs Ruby in a location that rbenv (from RPM) can manage, thereby allowing several version to co-exist. Used https://github.com/imeyer/ruby-1.9.3-rpm SPEC file as guide.

%prep
%setup -n ruby-2.1.1

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"
mkdir -p opt/ruby
./configure \
  --enable-shared \
  --disable-rpath \
  --prefix="$RPM_BUILD_ROOT/opt/ruby"
#  --includedir=%{_includedir}/ruby \
#  --libdir=%{_libdir} \

make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT
# delete source 
rm -rf $RPM_BUILD_ROOT/usr/src
# place in correct dirs
mkdir -p $RPM_BUILD_ROOT/opt/rbenv-ruby_2.1.1
mv $RPM_BUILD_ROOT/usr/* $RPM_BUILD_ROOT/opt/rbenv-ruby_2.1.1/

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo " "
echo "rbenv enabled Ruby has been installed in /opt/rbenv-ruby_2.1.1"

%files
%dir /opt/rbenv-ruby_2.1.1
/opt/rbenv-ruby_2.1.1/*

%changelog
* Mon Mar 24 2014 Guy Gershoni <guy@conchus.com> - 1-0.2.1.1
- Initial version of the package
