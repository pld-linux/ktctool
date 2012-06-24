Summary:	GUI for network bandwidth management in Linux
Summary(pl):	Graficzny interfejs do zarz�dzania pasmem sieci w Linuksie
Name:		ktctool
Version:	1.0
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.zone.ee/ktc/Ktctool.zip
# Source0-md5:	ea0f68247d05d1c2c15556ddd873456a
URL:		http://fr.ee/ktctool/
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
Requires:	iproute2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ktctool is a graphical interface for network bandwidth management in
Linux. There already exists commandline program tc for this purpose.
Ktctool is meant to be a graphical user interface to tc. tc is a part
of iproute2 and controls Quality of Service support in Linux (included
in kernel).

%description -l pl
Ktctool to graficzny interfejs do zarz�dzania pasmem sieci w Linuksie.
Istnieje ju� w tym celu dzia�aj�cy z linii polece� program tc. Ktctool
ma by� graficznym interfejsem u�ytkownika do tc. tc jest cz�ci�
iproute2 i steruje obs�ug� QoS (Quality of Service - jako�ci us�ug) w
j�drze Linuksa.

%prep
%setup -q -n %{name}

%build
install /usr/share/automake/config.* admin
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{name}/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/*/*/*/*.png
