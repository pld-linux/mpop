Summary:	mpop retrieves mails from POP3 mailboxes
Summary(pl.UTF-8):	mpop - pobieranie listów ze skrzynek POP3
Name:		mpop
Version:	1.0.7
Release:	1
License:	GPL v2
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/mpop/%{name}-%{version}.tar.bz2
# Source0-md5:	61dbe028aa86b1961056a80a5b78eadd
Patch0:		%{name}-home_etc.patch
URL:		http://mpop.sourceforge.net/
BuildRequires:	gnutls-devel >= 1.2.0
BuildRequires:	gsasl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mpop is a small, fast, and portable POP3 client. Its features include
header-based email filtering (filter junk mail before downloading it),
delivery to mbox files, maildir folders, or a mail delivery agent, a
very fast POP3 implementation, many authentication methods, and good
support for TLS/SSL.

%description -l pl.UTF-8
mpop to mały, szybki i przenośny klient POP3. Jego możliwości obejmują
filtrowanie listów w oparciu o nagłówki (filtrowanie niechcianej
poczty przed jej ściągnięciem), dostarczanie do plików mbox albo MDA,
bardzo szybką implementację POP3, wiele metod uwierzytelniania oraz
dobrą obsługę TLS/SSL.

%prep
%setup -q
%patch0 -p1

%build
%configure
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
