#
# Conditional build:
%bcond_with	gsasl	# with GNU SASL support instead of built-it authentication code
#
Summary:	mpop retrieves mails from POP3 mailboxes
Summary(pl):	mpop - pobieranie listów ze skrzynek POP3
Name:		mpop
Version:	0.8.3
Release:	1
License:	GPL v2
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/mpop/%{name}-%{version}.tar.bz2
# Source0-md5:	906cd16d0ed840ac5e2c75eb5a499832
Patch0:		%{name}-home_etc.patch
URL:		http://mpop.sourceforge.net/
%{?with_gsasl:BuildRequires:	gsasl-devel >= 0.2.4}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mpop is a small, fast, and portable POP3 client. Its features include
header-based email filtering (filter junk mail before downloading it),
delivery to mbox files, maildir folders, or a mail delivery agent, a
very fast POP3 implementation, many authentication methods, and good
support for TLS/SSL.

%description -l pl
mpop to ma³y, szybki i przeno¶ny klient POP3. Jego mo¿liwo¶ci obejmuj±
filtrowanie listów w oparciu o nag³ówki (filtrowanie niechcianej
poczty przed jej ¶ci±gniêciem), dostarczanie do plików mbox albo MDA,
bardzo szybk± implementacjê POP3, wiele metod uwierzytelniania oraz
dobr± obs³ugê TLS/SSL.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--%{?with_gsasl:en}%{!?with_gsasl:dis}able-gsasl \
	--with-ssl=openssl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS doc/{mpop.html,mpoprc.example}
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*.info*
%{_mandir}/man1/*
