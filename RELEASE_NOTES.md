# Table of Contents #

- [glite-info-dynamic-ge v7.2.0](#glite-info-dynamic-ge-v7.2.0)
- [glite-info-dynamic-ge v7.1.0](#glite-info-dynamic-ge-v7.1.0)
- [glite-info-dynamic-ge v7.0.0](#glite-info-dynamic-ge-v7.0.0)


## glite-info-dynamic-ge v7.2.0 ##

### Release notes ###

#### Features ####
 * UNIVA milisecond precision (for time reporting) support (GGUS #109287).
 * Support for both HH:MM:SS and number time formats (GGUS #102417).

#### Fixed Issues ####
 * Added sanity check for memory values (rss<=vmem) (GGUS #104815).



## glite-info-dynamic-ge v7.1.0 ##

### Release notes ###

#### Features ####
 * New default GLUE/GLUE2 values strategy compliance (GGUS #97721).
 * UNIVA GridEngine version support (GGUS #104815).

#### Fixed Issues ####
 * Missing GLUE2 attributes added (GGUS #82902, #104815, #102416).



## glite-info-dynamic-ge v7.0.0 ##

### Release notes ###

#### New Features ####
 * Cache mechanism for qstat data (GGUS #78607).

#### Fixed Issues ####
 * Missing GLUE attributes due to syntax bug (GGUS #83352, #90353).
 * Version string for OGS/GE (GGUS #90353).
 * Segmentation fault when parsing big qstat XML files (GGUS #93506).
 * /etc/lrms directory creation (GGUS #94312).

#### Configuration ####
 Information provider script has been renamed to `glite-info-dynamic-ge`. To make GIP plugins aware of the change one can either:
   * Run YAIM configuration (`config_gip_sge` will be enough).
 or:
    * Manually editing `/var/lib/bdii/gip/plugin/glite-info-dynamic-ce` file to reflect the change.
