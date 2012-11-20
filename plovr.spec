%define		rel	0.1
%include	/usr/lib/rpm/macros.java
Summary:	plovr: a Closure build tool
Name:		plovr
Version:	0.1
Release:	0.201210.%{rel}
License:	Apache v2.0
Group:		Applications/WWW
Source0:	https://plovr.googlecode.com/files/plovr-eba786b34df9.jar
# Source0-md5:	20eac8ccc4578676511cf7ccbfc65100
Source1:	%{name}.sh
URL:		http://www.plovr.com/
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
plovr is a build tool that dynamically recompiles JavaScript and
Closure Template code. It is designed to simplify Closure development,
and to make it more enjoyable.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}}
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}

# jars
cp -p %{SOURCE0} $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_javadir}/*.jar
