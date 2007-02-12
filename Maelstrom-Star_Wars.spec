Summary:	Rockin' asteroids game - Star Wars theme
Summary(pl.UTF-8):   Gra, w której strzelasz do asteroidów - motyw Gwiezdne Wojny
Name:		Maelstrom-Star_Wars
Version:	1
Release:	3
License:	unknown
Group:		X11/Applications/Games
# Source0-md5:	0cc78e3b844517bd226766312bb5c32c
Source0:	http://www.devolution.com/~slouken/projects/Maelstrom/add-ons/Star_Wars.zip
URL:		http://www.devolution.com/~slouken/projects/Maelstrom/add-ons.html
Requires:	Maelstrom
Obsoletes:	Maelstrom-1980
Obsoletes:	Maelstrom-Star_Trek
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamedir	%{_datadir}/Maelstrom

%description
Star Wars theme for Maelstrom.

%description -l pl.UTF-8
Motyw Gwiezdne Wojny dla Maelstroma.

%prep
%setup -q -n Star_Wars

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gamedir}

install "%Maelstrom Sounds" $RPM_BUILD_ROOT%{_gamedir}/Maelstrom_Sounds.bin
install "%Maelstrom Sprites" $RPM_BUILD_ROOT%{_gamedir}/Maelstrom_Sprites.bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{_gamedir}/*
