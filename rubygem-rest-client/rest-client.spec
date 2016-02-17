%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name rest-client

Summary: Simple REST client for Ruby, inspired by microframework syntax for specifying actions
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.6.7
Release: 4%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/archiloque/rest-client
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix_ruby}rubygems
%if 0%{?el6} && 0%{!?scl:1}
Requires: %{?scl_prefix_ruby}ruby(abi)
%else
Requires: %{?scl_prefix_ruby}ruby(release)
%endif
Requires: %{?scl_prefix_ror}rubygem(mime-types) >= 1.16
Requires: %{?scl_prefix}rubygem(netrc)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
A simple Simple HTTP and REST client for Ruby, inspired by the Sinatra
microframework style of specifying actions: get, put, post, delete.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}

%if 0%{?el6} && 0%{!?scl:1}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force --rdoc --bindir .%{_bindir} %{SOURCE0}
%{?scl:"}
%else
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}
%endif

mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)

%{_bindir}/restclient

%{gem_dir}/gems/%{gem_name}-%{version}/

%doc %{gem_dir}/doc/%{gem_name}-%{version}

%doc %{gem_instdir}/README.rdoc

%doc %{gem_instdir}/history.md

%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.6.7-4
- Fix build errors and modernise specs (dcleal@redhat.com)
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.6.7-3
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Tue May 27 2014 Dominic Cleal <dcleal@redhat.com> 1.6.7-2
- Remove specific ABI version (dcleal@redhat.com)

* Tue May 27 2014 Dominic Cleal <dcleal@redhat.com> 1.6.7-1
- Update to 1.6.7, support RHEL 7

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.6.1-4
- BR rubygems-devel (msuchy@redhat.com)

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 1.6.1-3
- new package built with tito

* Wed Nov 10 2010 Shannon Hughes <shughes@redhat.com> 1.6.1-2
- - mass gem update - updated specs for fedora guidelines - removed dev
  dependencies in specs (shughes@redhat.com)

* Fri Nov 05 2010 Shannon Hughes <shughes@redhat.com> - 1.6.1-1
- Initial package