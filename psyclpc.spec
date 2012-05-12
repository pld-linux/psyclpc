Summary:	Compiler for psyc LPC
Summary(pl.UTF-8):	Kompilator dla psyc LPC
Name:		psyclpc
Version:	20111122
Release:	1
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://www.psyced.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	defb6e3a4e26ed20b2c4f0e9448054b3
URL:		http://www.psyced.org
#Patch0: %{name}-doc-install.patch
BuildRequires:	help2man
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compiler for the psyc variant of LPC.

%description -l pl.UTF-8
Kompilator dla wariantów psyc dla LPC.

%prep
%setup -q -n %{name}
#%patch0 -p1

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
%{_mandir}/man1/*
