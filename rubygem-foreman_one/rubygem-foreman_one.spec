# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_one

%define rubyabi 1.9.1
%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d
%global foreman_pluginconf_dir %{foreman_dir}/config/settings.plugins.d

Summary:    Provision and manage OpenNebula VMs from Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.2
Release:    2%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman-one
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires:   foreman-compute >= 1.6.0
Requires:   %{?scl_prefix}rubygem(fog) >= 1.23.0
Requires:   %{?scl_prefix}rubygem(opennebula) >= 4.4.0

%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi) >= %{rubyabi}
%endif
Requires: %{?scl_prefix_ruby}rubygems

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(abi) >= %{rubyabi}
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-one
Provides: foreman-plugin-opennebula
Provides: foreman-one
Provides: foreman-opennebula
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
This plugin enables provisioning and managing OpenNebula VMs in Foreman.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_bundlerd_dir}
cat <<GEMFILE > %{buildroot}%{foreman_bundlerd_dir}/%{gem_name}.rb
gem '%{gem_name}'
GEMFILE

%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/lib
%{gem_instdir}/locale
%exclude %{gem_cache}
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/test
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb
%doc %{gem_instdir}/LICENSE

%exclude %{gem_cache}

%files doc
%doc %{gem_instdir}/README.md

%changelog
* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.2-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Aug 13 2014 Dominic Cleal <dcleal@redhat.com> 0.2-1
- new package built with tito