Summary:	DanSoft Net Utils
Name:		ds_net_utils
Version:	0.2
Release:	1
License:	GPLv2+
Group:		Networking/Other
Url:		http://dansoft.krasnokamensk.ru
Source0:	http://dansoft.krasnokamensk.ru/data/1017/%{name}-%{version}.tar.gz
BuildRequires:	qt4-devel

%description
DanSoft Net Utils:
 - ping
 - what is my ip
 - Looking Glass

%prep
%setup -q

%build
%qmake_qt4
%make

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 ping/ds_ping %{buildroot}%{_bindir}/ds_ping
install -m 755 lg/ds_lg %{buildroot}%{_bindir}/ds_lg
install -m 755 whatismyip/ds_whatismyip %{buildroot}%{_bindir}/ds_whatismyip

%files
%{_bindir}/ds_ping
%{_bindir}/ds_lg
%{_bindir}/ds_whatismyip

