%global pkg_name slf4j
%{?scl:%scl_package %{pkg_name}}
%{?java_common_find_provides_and_requires}

# Copyright (c) 2000-2009, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.7.4
Release:        3.22%{?dist}
Epoch:          0
Summary:        Simple Logging Facade for Java
# the log4j-over-slf4j and jcl-over-slf4j submodules are ASL 2.0, rest is MIT
License:        MIT and ASL 2.0
URL:            http://www.slf4j.org/
Source0:        http://www.slf4j.org/dist/%{pkg_name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}javapackages-tools
BuildRequires:  %{?scl_prefix}ant >= 0:1.6.5
BuildRequires:  %{?scl_prefix}ant-junit >= 0:1.6.5
BuildRequires:  %{?scl_prefix_maven}javassist >= 0:3.4
BuildRequires:  %{?scl_prefix}junit >= 0:3.8.2
BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix_maven}maven-antrun-plugin
BuildRequires:  %{?scl_prefix_maven}maven-compiler-plugin
BuildRequires:  %{?scl_prefix_maven}maven-install-plugin
BuildRequires:  %{?scl_prefix_maven}maven-jar-plugin
BuildRequires:  %{?scl_prefix_maven}maven-javadoc-plugin
BuildRequires:  %{?scl_prefix_maven}maven-resources-plugin
BuildRequires:  %{?scl_prefix_maven}maven-source-plugin
BuildRequires:  %{?scl_prefix_maven}maven-site-plugin
BuildRequires:  %{?scl_prefix_maven}maven-doxia-sitetools
BuildRequires:  %{?scl_prefix_maven}maven-surefire-plugin
BuildRequires:  %{?scl_prefix_maven}maven-surefire-provider-junit
BuildRequires:  %{?scl_prefix_maven}maven-plugin-build-helper
BuildRequires:  %{?scl_prefix}log4j
BuildRequires:  %{?scl_prefix}apache-commons-logging
BuildRequires:  %{?scl_prefix_maven}cal10n

Requires:       %{?scl_prefix}runtime

%description
The Simple Logging Facade for Java or (SLF4J) is intended to serve
as a simple facade for various logging APIs allowing to the end-user
to plug in the desired implementation at deployment time. SLF4J also
allows for a gradual migration path away from
Jakarta Commons Logging (JCL).

Logging API implementations can either choose to implement the
SLF4J interfaces directly, e.g. NLOG4J or SimpleLogger. Alternatively,
it is possible (and rather easy) to write SLF4J adapters for the given
API implementation, e.g. Log4jLoggerAdapter or JDK14LoggerAdapter..

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
This package provides %{summary}.

%package parent
Summary:        Parent POM for %{pkg_name}

%description parent
Parent POM for %{pkg_name}

%package api
Summary:        API for %{pkg_name}

%description api
This package provides API for %{pkg_name}.

%package simple
Summary:        simple module for %{pkg_name}
Requires:       %{name} = %{version}-%{release}

%description simple
This package provides simple module for %{pkg_name}.

%package nop
Summary:        nop module for %{pkg_name}

%description nop
This package provides nop module for %{pkg_name}.

%package jdk14
Summary:        jdk14 module for %{pkg_name}

%description jdk14
This package provides jdk14 module for %{pkg_name}.

%package -n %{?scl_prefix}jcl-over-slf4j
Summary:        jcl-over-slf4j module for %{pkg_name}

%description -n %{?scl_prefix}jcl-over-slf4j
This package provides jcl-over-slf4j module for %{pkg_name}.

%package -n %{?scl_prefix}log4j-over-slf4j
Summary:        log4j-over-slf4j module for %{pkg_name}

%description -n %{?scl_prefix}log4j-over-slf4j
This package provides log4j-over-slf4j module for %{pkg_name}.

%package -n %{?scl_prefix}jul-to-slf4j
Summary:        jul-to-slf4j module for %{pkg_name}

%description -n %{?scl_prefix}jul-to-slf4j
This package provides jul-to-slf4j module for %{pkg_name}.

%package site
Summary:        site module for %{pkg_name}
Requires:       %{name} = %{version}-%{release}

%description site
This package provides site module for %{pkg_name}.

%package migrator
Summary:        migrator module for %{pkg_name}
Requires:       %{name} = %{version}-%{release}

%description migrator
This package provides migrator module for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
find . -name "*.jar" | xargs rm
cp -p %{SOURCE1} APACHE-LICENSE

%pom_disable_module integration
%pom_disable_module osgi-over-slf4j
%pom_disable_module slf4j-ext
%pom_disable_module slf4j-log4j12
%pom_disable_module slf4j-jcl
%pom_remove_plugin :maven-source-plugin

# Because of a non-ASCII comment in slf4j-api/src/main/java/org/slf4j/helpers/MessageFormatter.java
%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>ISO-8859-1</project.build.sourceEncoding>"

# Fix javadoc links
%pom_xpath_remove "pom:links"
%pom_xpath_inject "pom:plugin[pom:artifactId[text()='maven-javadoc-plugin']]/pom:configuration" "
    <detectJavaApiLink>false</detectJavaApiLink>
    <isOffline>false</isOffline>
    <links><link>/usr/share/javadoc/java</link></links>"

# remove wagon-ssh build extension
%pom_xpath_remove pom:build/pom:extensions

# dos2unix
find -name "*.css" -o -name "*.js" -o -name "*.txt" | \
    xargs -t %{__perl} -pi -e 's/\r$//g'

# The general pattern is that the API package exports API classes and does
# not require impl classes. slf4j was breaking that causing "A cycle was
# detected when generating the classpath slf4j.api, slf4j.nop, slf4j.api."
# The API bundle requires impl package, so to avoid cyclic dependencies
# during build time, it is necessary to mark the imported package as an
# optional one.
# Reported upstream: http://bugzilla.slf4j.org/show_bug.cgi?id=283
sed -i "/Import-Package/s/.$/;resolution:=optional&/" slf4j-api/src/main/resources/META-INF/MANIFEST.MF
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_build -f -s
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install

# Compat symlinks
(cd $RPM_BUILD_ROOT/%{_javadir}/%{pkg_name}; for jar in %{pkg_name}-*; do
    ln -s $jar ${jar/%{pkg_name}-/}; done)
%{?scl:EOF}

%files
%doc LICENSE.txt APACHE-LICENSE
%{_javadir}/%{pkg_name}

%files parent -f .mfiles-%{pkg_name}-parent
%dir %{_mavenpomdir}/%{pkg_name}
%files api -f .mfiles-%{pkg_name}-api
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files simple -f .mfiles-%{pkg_name}-simple
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files nop -f .mfiles-%{pkg_name}-nop
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files jdk14 -f .mfiles-%{pkg_name}-jdk14
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files -n %{?scl_prefix}jcl-over-slf4j -f .mfiles-jcl-over-slf4j
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files -n %{?scl_prefix}log4j-over-slf4j -f .mfiles-log4j-over-slf4j
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files -n %{?scl_prefix}jul-to-slf4j -f .mfiles-jul-to-slf4j
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files site -f .mfiles-%{pkg_name}-site
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files migrator -f .mfiles-%{pkg_name}-migrator
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt APACHE-LICENSE

%changelog
* Thu Jan 15 2015 Michael Simacek <msimacek@redhat.com> - 0:1.7.4-3.22
- All subpackages should own common directory

* Thu Jan 15 2015 Michael Simacek <msimacek@redhat.com> - 0:1.7.4-3.21
- All subpackages should own common directory

* Wed Jan 14 2015 Michal Srb <msrb@redhat.com> - 0:1.7.4-3.20
- Fix directory ownership

* Wed Jan 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.4-3.19
- Add requires on SCL filesystem package

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 0:1.7.4-3.18
- Mass rebuild 2015-01-13

* Mon Jan 12 2015 Michael Simacek <msimacek@redhat.com> - 0:1.7.4-3.17
- Rebuild to regenerate requires

* Fri Jan 09 2015 Michal Srb <msrb@redhat.com> - 0:1.7.4-3.16
- Mass rebuild 2015-01-09

* Thu Jan 08 2015 Michal Srb <msrb@redhat.com> - 1.7.4-3.15
- Fix FTBFS

* Tue Dec 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.4-3.14
- Migrate requires and build-requires to rh-java-common

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.4-3.13
- Mass rebuild 2014-12-15

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.4-3.12
- Rebuild for rh-java-common collection

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.4-3.11
- Mass rebuild 2014-05-26

* Tue Mar 04 2014 Michael Simacek <msimacek@redhat.com> - 0:1.7.4-3.10
- Remove wagon-ssh build extension

* Fri Feb 28 2014 Michael Simacek <msimacek@redhat.com> - 0:1.7.4-3.9
- Correctly SCLize subpackages

* Fri Feb 28 2014 Michael Simacek <msimacek@redhat.com> - 0:1.7.4-3.8
- Split into subpackages
- Add missing maven-wagon-ssh BR

* Thu Feb 20 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.4-3.7
- Disable unneeded modules

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.4-3.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.4-3.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.4-3.4
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.4-3.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.4-3.2
- Don't use %%{_bindir} to call find or xargs utilities
- Remove manual subpackage

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.4-3.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.4-3.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 01.7.4-3
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.4-2
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Mar 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.4-1
- Update to upstream version 1.7.4

* Fri Mar 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.3-1
- Update to upstream version 1.7.3

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:1.7.2-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan  9 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.2-7
- Fix install location of manual

* Tue Jan  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.2-6
- Rebuild to generate maven provides

* Fri Nov 30 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.2-5
- Build with xmvn

* Wed Nov 21 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.2-4
- Install Apache license file
- Resolves: rhbz#878996

* Thu Nov 15 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.2-3
- Avoid cyclic OSGi dependencies

* Thu Nov 08 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.7.2-2
- Fix license to ASL 2.0 and MIT
- Update to add_maven_depmap macro
- Use generated .mfiles list
- Small packaging cleanups

* Mon Oct 15 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.2-1
- Update to upstream version 1.7.2

* Mon Sep 17 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.1-1
- Update to upstream version 1.7.1

* Mon Sep 10 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.7.0-1
- Update to upstream version 1.7.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.6.6-1
- Update to upstream version 1.6.6
- Convert patches to POM macros

* Fri Jan 13 2012 Ville Skyttä <ville.skytta@iki.fi> - 0:1.6.1-5
- Crosslink with local JDK API docs.

* Fri Jan 13 2012 Ville Skyttä <ville.skytta@iki.fi> - 0:1.6.1-4
- Specify explicit source encoding to fix build with Java 1.7.
- Remove no longer needed javadoc dir upgrade hack.

* Wed Jun 8 2011 Alexander Kurtakov <akurtako@redhat.com> 0:1.6.1-3
- Build with maven 3.x.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Alexander Kurtakov <akurtako@redhat.com> 0:1.6.1-1
- Update to new upstream version.
- Various guidelines fixes.

* Wed Sep 8 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.5.11-3
- Add maven-site-pugin BR.
- Use new package names.

* Wed Sep 8 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.5.11-2
- Skip installing tests jar that is no longer produced.
- Use javadoc aggregate.
- Use mavenpomdir macro.

* Thu Feb 25 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.5.11-1
- Update to 1.5.11.
- Drop depmap and component info files.

* Wed Feb 10 2010 Mary Ellen Foster <mefoster at gmail.com> 0:1.5.10-5
- Require cal10n

* Wed Feb 10 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.5.10-4
- Fix javadoc files.

* Wed Feb 10 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.5.10-3
- BR maven-plugin-build-helper.

* Wed Feb 10 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.5.10-2
- BR cal10n.

* Wed Feb 10 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.5.10-1
- Update to upstream 1.5.10.

* Fri Sep 4 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.5.8-5
- Skip tests.

* Wed Sep 2 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.5.8-4
- Fix other line lenghts.

* Wed Sep 2 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.5.8-3
- Fix permissions.
- Fixed descriptions.
- Fix file lengths.

* Wed Sep 2 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.5.8-2
- Adapt for Fedora.

* Wed Jul 29 2009 Yong Yang <yyang@redhat.com> 0:1.5.8-1
- 1.5.8
- Replace slf4j-1.5.6-integration-tests-current-only.patch with
  slf4j-1.5.8-skip-integration-tests.patch because of the failure of "testMatch"

* Fri Jun 12 2009 Ralph Apel <r.apel at r-apel.de> 0:1.5.6-2
- Add -ext jar, depmap and pom
- Save jcl104-over-slf4j as symlink

* Tue Feb 18 2009 David Walluck <dwalluck@redhat.com> 0:1.5.6-1
- 1.5.6
- add repolib
- fix file eol
- fix Release tag

* Fri Jul 18 2008 David Walluck <dwalluck@redhat.com> 0:1.5.2-2
- use excalibur for avalon
- remove javadoc scriptlets
- GCJ fixes
- fix maven directory ownership
- fix -bc --short-circuit by moving some of %%build to %%prep

* Sun Jul 06 2008 Ralph Apel <r.apel at r-apel.de> 0:1.5.2-1.jpp5
- 1.5.2

* Mon Feb 04 2008 Ralph Apel <r.apel at r-apel.de> 0:1.4.2-2jpp
- Fix macro misprint
- Add maven2-plugin BRs

* Wed Jul 18 2007 Ralph Apel <r.apel at r-apel.de> 0:1.4.2-1jpp
- Upgrade to 1.4.2
- Build with maven2
- Add poms and depmap frags
- Add gcj_support option

* Mon Jan 30 2006 Ralph Apel <r.apel at r-apel.de> 0:1.0-0.rc5.1jpp
- First JPackage release.
