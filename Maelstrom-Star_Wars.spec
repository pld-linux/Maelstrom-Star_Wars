Summary:	Rockin' asteroids game - Star Wars theme
Summary(pl):	Gra, w której strzelasz do asteroidów - temat Gwiezdne Wojny
Name:		Maelstrom-Star_Wars
Version:	1
Release:	1
License:	dunno
Group:		X11/Application/Games
Source0:	http://www.devolution.com/~slouken/Maelstrom/add-ons/Star_Wars.tar.gz
URL:		http://www.devolution.com/~slouken/Maelstrom/add-ons/
Requires:	Maelstrom
Obsoletes:	Maelstrom-1980
Obsoletes:	Maelstrom-Star_Trek
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Star Wars theme for Maelstrom.

%description -l pl
Temat Gwiezdne Wojny dla Maelstroma.

%prep
%setup -q -n Star_Wars

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/games/Maelstrom

install %* $RPM_BUILD_ROOT%{_prefix}/games/Maelstrom

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{_prefix}/games/Maelstrom/*
