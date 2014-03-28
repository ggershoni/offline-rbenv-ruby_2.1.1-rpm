offline-rbenv-ruby_2.1.1-rpm
==========================

RPM install of Ruby 2.1.1 which integrates with [Offline rbenv RPM](https://github.com/ggershoni/offline-rbenv-rpm)

This RPM does not download anything from the Internet.  The idea is to allow you to install Ruby (for rbenv) on a production environment where internet access is limited.

## Building RPM 

### Useful sites

http://wiki.centos.org/HowTos/SetupRpmBuildEnvironment

http://www.lamolabs.org/blog/164/centos-rpm-tutorial-1/

http://www.lamolabs.org/blog/6837/centos-rpm-tutorial-part-3-building-your-own-rpm-of-jboss/



### Prepare

Need to install the following packages to allow you to build RPMs:
```
yum install rpm-build redhat-rpm-config
```

This RPM has many build dependencies (packages we need to build it).  The following simplifies installing those:
```
yum install yum-utils
```
Now you can use yum-builddep... see "Building RPM"

#### Centos/RHEL 5.x

For EL5 you will also need:
```
yum install buildsys-macros
```

### Building RPM

Some packages are not in default repos so get:

 * libyaml and libyaml-devel from http://pkgs.repoforge.org/libyaml/

Remember you can download and install RPMs in one go i.e.:
```
yum install http://pkgs.repoforge.org/libyaml/libyaml-0.1.4-1.el6.rf.x86_64.rpm
```

Building RPMs should never be done as root so:
```
adduser rpmbuild
su - rpmbuild
git clone https://github.com/ggershoni/offline-rbenv-ruby_2.1.1-rpm
echo '%_topdir %(echo $HOME)/offline-rbenv-ruby_2.1.1-rpm' > ~/.rpmmacros 
cd offline-rbenv-ruby_2.1.1-rpm
sudo yum-builddep SPECS/rbenv-ruby.spec
rpmbuild -ba SPECS/rbenv-ruby.spec
```

## Install RPM

Below is for Centos/RHEL 5 but if EL 6 rpm in repo please update URL and RPM to suit.

```
wget --no-check-certificate https://github.com/ggershoni/offline-rbenv-ruby_2.1.1-rpm/raw/master/RPMS/x86_64/rbenv-ruby_2.1.1-p76-1.el5.x86_64.rpm
sudo yum install --nogpgcheck rbenv-ruby_2.1.1-p76-1.el5.x86_64.rpm
```

## TODO
* Currently all under /opt... not good.  Need to structure so follows FSH.

