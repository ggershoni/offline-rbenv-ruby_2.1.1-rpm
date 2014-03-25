%define _prefix /opt/ruby_2.1.1

Name:		rbenv-ruby_2.1.1
Version:	p76 
Release: 	1%{?dist:%{dist}}
Group: 		Development/Languages
Summary: 	A ruby instance that can co-exist with other instances in the rbenv (RPM) ecosystem.
License: 	MIT
URL: 		https://https://github.com/ggershoni/offline-rbenv-ruby_2.1.1-rpm
Source0: 	ruby-2.1.1.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires: 	redhat-rpm-config readline libyaml libyaml-devel readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make libffi-devel openssl-devel
Requires: 	libyaml openssl

%description
Installs Ruby in a location that rbenv (from RPM) can manage, thereby allowing several version to co-exist. Used https://github.com/imeyer/ruby-1.9.3-rpm SPEC file as guide.

%prep
%setup -n ruby-2.1.1

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"
%configure \
  --disable-rpath 
#  --enable-shared \
#  --includedir=%{_includedir}/ruby \
#  --libdir=%{_libdir} \

make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT
# delete source, doc and debug (all in usr dir which we don't want to install)
rm -rf $RPM_BUILD_ROOT/usr
# setup symbolic link and global version for users
install -m 0755 -d $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
cat > $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/%{name}.sh <<END_OF_RBENV_RUBY_PROFILE
# add rbenv ruby path symlink
if [ ! -h ~/.rbenv/versions/2.1.1 ] 
  then
    ln -s %{_prefix} ~/.rbenv/versions/2.1.1
    eval "$(rbenv rehash)"
fi
# add global ruby version if needed.
if [ ! -e ~/.rbenv/version ]
  then
    echo "2.1.1" > ~/.rbenv/version
fi
END_OF_RBENV_RUBY_PROFILE

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo " "
echo "rbenv enabled Ruby has been installed in /opt/rbenv-ruby_2.1.1"

%files
%dir %{_prefix}
%{_prefix}/*
%{_sysconfdir}/profile.d
%{_sysconfdir}/profile.d/rbenv-ruby_2.1.1.sh

%changelog
* Mon Mar 24 2014 Guy Gershoni <guy@conchus.com> - 1-0.2.1.1
- Initial version of the package
