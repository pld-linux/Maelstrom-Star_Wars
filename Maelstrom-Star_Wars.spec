Summary:	Rockin' asteroids game - Star Wars theme
Summary(pl):	Gra, w której strzelasz do asteroidów - motyw Gwiezdne Wojny
Name:		Maelstrom-Star_Wars
Version:	1
Release:	2
License:	dunno
Group:		X11/Applications/Games
Source0:	http://www.devolution.com/~slouken/Maelstrom/add-ons/Star_Wars.tar.gz
URL:		http://www.devolution.com/~slouken/Maelstrom/add-ons/
Requires:	Maelstrom
Obsoletes:	Maelstrom-1980
Obsoletes:	Maelstrom-Star_Trek
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamedir	%{_datadir}/Maelstrom

%description
Star Wars theme for Maelstrom.

%description -l pl
Motyw Gwiezdne Wojny dla Maelstroma.

%prep
%setup -q -n Star_Wars

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gamedir}

install %* $RPM_BUILD_ROOT%{_gamedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{_gamedir}/*
