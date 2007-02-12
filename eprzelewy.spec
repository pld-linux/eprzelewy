
%define		_pre	pre1

Summary:	Program to print transfers
Summary(pl.UTF-8):   Program do drukowania przelewów
Name:		eprzelewy
Version:	1.0.2
Release:	1.%{_pre}.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.e-linux.pl/modules/e-przelewy/%{name}-%{version}_%{_pre}.tar.gz
# Source0-md5:	ded7949a2d8b25f35db82af294207241
Patch0:		%{name}-desktop.patch
URL:		http://www.e-linux.pl/modules/e-przelewy/
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
e-Przelewy is a GUI program to print transfers. It's targeted to
Polish users and contains options specific to Polish tax system etc.

%description -l pl.UTF-8
System e-Przelewy został przygotowany z myślą o tych użytkownikach,
którzy chcą korzystać z Linuksa w codziennej pracy zawodowej. Jest to
wszechstronny program, pracujący w trybie graficznym (okienkowym np.
KDE, GNOME, fluxbox). Daje on możliwość prostej obsługi wszelkiego
rodzaju przelewów. Obsługuje: przelewy zwykle, wpłaty, przelewy na
ZUS, wpłaty podatku dla Urzędu Skarbowego (US). Możliwe jest także
wykonywanie nadruków na oryginalnych drukach z poczty, banku lub
urzędu. Wbudowana w program baza kontrahentów sprawia, że dokonanie
przelewu na dowolne konto, czy to do ZUS, US jest w zasięgu kilku
ruchów myszą. Równie prosta jest obsługa przelewów, które wykonujemy
cyklicznie np. wpłaty ZUS, wystarczy wówcza s otworzyć z historii
przelew z zeszłego miesiąca i jedynie zmienić kwotę lub tytuł.

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
