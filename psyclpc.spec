Summary:	Compiler for psyc LPC
Name:		psyclpc
Version:	20090321
Release:	1
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://www.psyced.org/files/psyclpc-20090321.tar.bz2
# Source0-md5:	96b365e2d89942b086138b29693e191c
URL:		http://www.psyced.org
Patch0:	%{name}-doc-install.patch
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
BuildRequires: 	help2man
BuildRequires: 	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compiler for the psyc variant of LPC.

%prep
%setup -q
%patch0 -p1

%build
cd src
%configure \
	--with-malloc=sysmalloc \
	--enable-use-ipv6 \
	--enable-use-mccp \
	--enable-use-mysql \
	--enable-use-pgsql \
	--enable-use-sqlite \
	--enable-use-json \
	--enable-use-srv

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd src
%{__make} install-driver install-utils \
	BINDIR=$RPM_BUILD_ROOT/%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT/%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%_mandir/man1/*
