Summary:	A better soundmixer tool
Summary(pl):	Narzêdzie do obs³ugi miksera
Name:		xqmixer
Version:	2.0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.webeifer.de/alwin/programs/download/xqmixer/%{name}-%{version}.tar.gz
# Source0-md5:	7f39b74afd013e9427c558959a7a96af
Patch0:		%{name}-gcc33.patch
URL:		http://www.webeifer.de/alwin/programs/xqmixer/
BuildRequires:	kdelibs-devel >= 3.0
BuildRequires:	qt-devel >= 3.0
BuildRequires:	rpmbuild(macros) >= 1.129
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
%patch -p1

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Multimedia/xqmixer.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xqmixer
%{_iconsdir}/hicolor/*/apps/*.png
%{_desktopdir}/kde/*.desktop
