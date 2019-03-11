%define debug_package %{nil}

%global gh_user hashicorp

Name:           terraform
Version:        0.11.13
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
%license %{name}-%{version}/src/github.com/%{gh_user}/%{name}/LICENSE
%doc %{name}-%{version}/src/github.com/%{gh_user}/%{name}/{BUILDING.md,CHANGELOG.md,README.md}
%{_bindir}/%{name}


%changelog
* Thu Mar 12 2019 Jamie Curnow <jc@jc21.com> 0.11.13-1
- Initial spec

