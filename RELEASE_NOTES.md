# glite-info-dynamic-ge v7.0.0

## Release notes 

### New Features
 * Cache mechanism for qstat data (GGUS #78607).

### Fixed Issues
 * Missing GLUE attributes due to syntax bug (GGUS #83352, #90353).
 * Version string for OGS/GE (GGUS #90353).
 * Segmentation fault when parsing big qstat XML files (GGUS #93506).
 * /etc/lrms directory creation (GGUS #94312).

### Configuration
 Information provider script has been renamed to `glite-info-dynamic-ge`. To make GIP plugins aware of the change one can either:

   * Run YAIM configuration (`config_gip_sge` will be enough).
 
 or:

   * Manually editing `/var/lib/bdii/gip/plugin/glite-info-dynamic-ce` file to reflect the change.

#### Cache Mechanism
 Note that the __cache mechanism is not enabled by default__. 
 
 To enable this feature one have to define the parameters listed below under `/etc/lrms/sge.conf`:

   * `cache_dir`       : path where the qstat data will be stored.
   * `cache_expiration`: time in seconds before re-creating the qstat cache.

### Available packages:
 * Scientific Linux 5: http://download.opensuse.org/repositories/home:/aloga:/ge-utils/sl5/noarch/glite-info-dynamic-ge-7.0.0-3.1.noarch.rpm
 * Scientific Linux 6: http://download.opensuse.org/repositories/home:/aloga:/ge-utils/sl6/noarch/glite-info-dynamic-ge-7.0.0-3.1.noarch.rpm
