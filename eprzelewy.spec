Summary:	Program to print transfers
Summary(pl):	Program do drukowania przelew�w
Name:		eprzelewy
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.e-linux.pl/modules/e-przelewy/%{name}-%{version}.tar.gz
# Source0-md5:	ad3280b7006c465d598566d3857ab423
Patch0:		%{name}-desktop.patch
URL:		http://www.e-linux.pl/modules/e-przelewy/
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
e-Przelewy is a GUI program to print transfers. It's targeted to
Polish users and contains options specific to Polish tax system etc.

%description -l pl
System e-Przelewy zosta� przygotowany z my�l� o tych u�ytkownikach,
kt�rzy chc� korzysta� z Linuksa w codziennej pracy zawodowej. Jest to
wszechstronny program, pracuj�cy w trybie graficznym (okienkowym np.
KDE, GNOME, fluxbox). Daje on mo�liwo�� prostej obs�ugi wszelkiego
rodzaju przelew�w. Obs�uguje: przelewy zwykle, wp�aty, przelewy na
ZUS, wp�aty podatku dla Urz�du Skarbowego (US). Mo�liwe jest tak�e
wykonywanie nadruk�w na oryginalnych drukach z poczty, banku lub
urz�du. Wbudowana w program baza kontrahent�w sprawia, �e dokonanie
przelewu na dowolne konto, czy to do ZUS, US jest w zasi�gu kilku
ruch�w mysz�. R�wnie prosta jest obs�uga przelew�w, kt�re wykonujemy
cyklicznie np. wp�aty ZUS, wystarczy w�wcza s otworzy� z historii
przelew z zesz�ego miesi�ca i jedynie zmieni� kwot� lub tytu�.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
export QTDIR=%{_prefix}
qmake przelewy.pro
# sed -e 's/-lqt /lqt-mt/g' -i Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D bin/eprzelewy $RPM_BUILD_ROOT%{_bindir}/eprzelewy
install -d $RPM_BUILD_ROOT%{_datadir}
cp -r share/%{name} $RPM_BUILD_ROOT%{_datadir}
install -D ./share/eprzelewy/icons/eprzelewy.desktop $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog FAQ README README.ENG
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/icons
%{_datadir}/%{name}/icons/*.png
%{_datadir}/%{name}/druki
%{_desktopdir}/*.desktop
