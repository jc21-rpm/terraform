%define debug_package %{nil}

%global gh_user hashicorp

Name:           terraform
Version:        0.12.1
Release:        1
Summary:        Write, Plan, and Create Infrastructure as Code.
Group:          Applications/System
License:        MPLv2.0
URL:            https://terraform.io/
BuildRequires:  golang >= 1.11
BuildRequires:  make which zip


%description
Terraform enables you to safely and predictably create, change, and improve
production infrastructure. It is an open source tool that codifies APIs into
declarative configuration files that can be shared amongst team members, treated
as code, edited, reviewed, and versioned.


%prep
wget https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
tar xzf v%{version}.tar.gz


%build
cd %{name}-%{version}
export GOPATH=$PWD
export PATH=${PATH}:${GOPATH}/bin
export XC_ARCH=amd64
export XC_OS=linux
mkdir -p src/github.com/%{gh_user}/%{name}
shopt -s extglob dotglob
mv !(src) src/github.com/%{gh_user}/%{name}
shopt -u extglob dotglob
pushd src/github.com/%{gh_user}/%{name}
make tools && make bin
popd


%install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 0755 %{name}-%{version}/src/github.com/%{gh_user}/%{name}/bin/%{name} $RPM_BUILD_ROOT%{_bindir}


%clean
rm -rf %{buildroot}


%files
%{_bindir}/%{name}


%changelog
* Wed Jun 5 2019 Jamie curnow <jc@jc21.com> 0.12.1-1
- v0.12.1

* Thu May 23 2019 Jamie curnow <jc@jc21.com> 0.12.0-1
- v0.12.0

* Mon May 20 2019 Jamie curnow <jc@jc21.com> 0.11.14-1
- v0.11.14

* Thu Mar 12 2019 Jamie Curnow <jc@jc21.com> 0.11.13-1
- Initial spec

