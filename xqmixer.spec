Summary:	A better soundmixer tool
Summary(pl):	Narzêdzie do obs³ugi miksera
Name:		xqmixer
Version:	1.11
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.webeifer.de/alwin/programs/download/xqmixer/%{name}-%{version}.tar.gz
# Source0-md5:	1390050954aae4212b1cde5301073085
URL:		http://www.webeifer.de/alwin/programs/xqmixer/xqmixer.html
BuildRequires:	kdelibs-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
XqMixer is a soundmixer, which supports USS/OSS. This version is build
for the KDE. It can save and restore various settings of mixer and has
a display for the current values of the various kinds of
mixer-settings.

%description -l pl
XqMixer jest mikserem d¼wiêku obs³uguj±cym USS/OSS. Tê wersjê
zbudowano dla KDE. Mo¿e ona zachowywaæ i przywracaæ ró¿ne ustawienia
miksera oraz wy¶wietla bie¿±ce warto¶ci rozmaitych ustawieñ miksera.

%prep
%setup -q

%build
%configure2_13 --with-qt-includes=/usr/X11R6/include/qt
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XqMixer
/opt/kde/share/doc/HTML/en/XqMixer/index.html
/opt/kde/share/applnk/Multimedia/XqMixer.kdelnk
%{_datadir}/icons/XqMixer.xpm
%{_datadir}/icons/mini/XqMixer.xpm
