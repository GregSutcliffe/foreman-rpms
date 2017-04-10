%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman-tasks-core

Summary: Code used both at Forman and Foreman proxy regarding tasks
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.2
Release: 1%{?foremandist}%{?dist}
Group: Development/Languages
License: GPLv3
URL: https://github.com/theforeman/foreman-tasks
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)

Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Common code used both at Forman and Foreman proxy regarding tasks

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE

%changelog
* Mon Apr 10 2017 Dominic Cleal <dominic@cleal.org> 0.1.2-1
- Update foreman-tasks-core to 0.1.2 (aruzicka@redhat.com)

* Tue Sep 13 2016 Dominic Cleal <dominic@cleal.org> 0.1.1-1
- new package built with tito

