%define debug_package %{nil}

%global gh_user hashicorp

Name:           terraform
Version:        0.12.29
Release:        1
Summary:        Write, Plan, and Create Infrastructure as Code.
Group:          Applications/System
License:        MPLv2.0
URL:            https://terraform.io/
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  golang >= 1.14, make, which, zip

%description
Terraform enables you to safely and predictably create, change, and improve
production infrastructure. It is an open source tool that codifies APIs into
declarative configuration files that can be shared amongst team members, treated
as code, edited, reviewed, and versioned.

%prep
%setup -q -n %{name}-%{version}

%build
go build -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Fri Jul 24 2020 Jamie Curnow <jc@jc21.com> 0.12.29-1
- v0.12.29

* Mon Jun 29 2020 Jamie Curnow <jc@jc21.com> 0.12.28-1
- v0.12.28

* Thu Jun 25 2020 Jamie Curnow <jc@jc21.com> 0.12.27-1
- v0.12.27

* Thu May 28 2020 Jamie Curnow <jc@jc21.com> 0.12.26-1
- v0.12.26

* Thu May 14 2020 Jamie Curnow <jc@jc21.com> 0.12.25-1
- v0.12.25

* Fri Mar 20 2020 Jamie Curnow <jc@jc21.com> 0.12.24-1
- v0.12.24

* Fri Mar 6 2020 Jamie Curnow <jc@jc21.com> 0.12.23-1
- v0.12.23

* Thu Feb 20 2020 Jamie Curnow <jc@jc21.com> 0.12.21-1
- v0.12.21

* Thu Jan 23 2020 Jamie Curnow <jc@jc21.com> 0.12.20-1
- v0.12.20

* Thu Jan 9 2020 Jamie Curnow <jc@jc21.com> 0.12.19-1
- v0.12.19

* Thu Dec 12 2019 Jamie Curnow <jc@jc21.com> 0.12.18-1
- v0.12.18

* Tue Dec 3 2019 Jamie Curnow <jc@jc21.com> 0.12.17-1
- v0.12.17

* Tue Nov 19 2019 Jamie Curnow <jc@jc21.com> 0.12.16-1
- v0.12.16

* Fri Nov 15 2019 Jamie Curnow <jc@jc21.com> 0.12.15-1
- v0.12.15

* Thu Nov 14 2019 Jamie Curnow <jc@jc21.com> 0.12.14-1
- v0.12.14

* Fri Nov 1 2019 Jamie Curnow <jc@jc21.com> 0.12.13-1
- v0.12.13

* Fri Oct 18 2019 Jamie Curnow <jc@jc21.com> 0.12.12-1
- v0.12.12

* Fri Oct 18 2019 Jamie Curnow <jc@jc21.com> 0.12.11-1
- v0.12.11

* Tue Oct 8 2019 Jamie Curnow <jc@jc21.com> 0.12.10-1
- v0.12.10

* Wed Sep 18 2019 Jamie Curnow <jc@jc21.com> 0.12.9-1
- v0.12.9

* Thu Sep 5 2019 Jamie Curnow <jc@jc21.com> 0.12.8-1
- v0.12.8

* Mon Aug 26 2019 Jamie Curnow <jc@jc21.com> 0.12.7-1
- v0.12.7

* Thu Aug 1 2019 Jamie Curnow <jc@jc21.com> 0.12.6-1
- v0.12.6

* Tue Jul 23 2019 Jamie Curnow <jc@jc21.com> 0.12.5-1
- v0.12.5

* Fri Jul 12 2019 Jamie Curnow <jc@jc21.com> 0.12.4-1
- v0.12.4

* Tue Jun 25 2019 Jamie Curnow <jc@jc21.com> 0.12.3-1
- v0.12.3

* Thu Jun 13 2019 Jamie Curnow <jc@jc21.com> 0.12.2-1
- v0.12.2

* Wed Jun 5 2019 Jamie Curnow <jc@jc21.com> 0.12.1-1
- v0.12.1

* Thu May 23 2019 Jamie Curnow <jc@jc21.com> 0.12.0-1
- v0.12.0

* Mon May 20 2019 Jamie Curnow <jc@jc21.com> 0.11.14-1
- v0.11.14

* Tue Mar 12 2019 Jamie Curnow <jc@jc21.com> 0.11.13-1
- Initial spec

