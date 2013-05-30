package=glite-info-dynamic-ge
name=$Name:  $
tag:=$(shell echo $(name) | sed 's/^[^:]*: //' )
version:=$(shell echo "$(tag)" | sed 's/^.*R_//' | sed 's/_/\./g')
release:=$(shell echo "$(version)" | sed 's/.*\.//')
version:=$(shell echo "$(version)" | sed 's/\(.*\)\.[0-9]*/\1/')

.PHONY: configure install clean rpm

all: configure

install: 
	@echo creating lrms directory ...
	@mkdir -p $(prefix)/etc/lrms/
	
	@echo installing ...
	@mkdir -p $(prefix)/usr/libexec/
        
	@install -m 0644 glite-info-dynamic-sge $(prefix)/usr/libexec/glite-info-dynamic-sge
clean::
	rm -rf rpmbuild 
	rm -rf RPMS
rpm:
	@mkdir -p  RPMS
	@mkdir -p  rpmbuild/RPMS/noarch
	@mkdir -p  rpmbuild/SRPMS/
	@mkdir -p  rpmbuild/SPECS/
	@mkdir -p  rpmbuild/SOURCES/
	@mkdir -p  rpmbuild/BUILD/
ifneq ("$(tag)","ame:")
	@sed -i 's/^Version:.*/Version: $(version)/' $(package).spec
	@sed -i 's/^Release:.*/Release: $(release)/' $(package).spec
endif
	@tar --gzip --exclude='*CVS*' -cf rpmbuild/SOURCES/${package}.src.tgz *
	rpmbuild -ba ${package}.spec
	cp rpmbuild/RPMS/noarch/*.rpm rpmbuild/SRPMS/*.rpm RPMS/.




