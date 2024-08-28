Name:		texlive-commutative-diagrams
Version:	71053
Release:	1
Summary:	CoDi: Commutative Diagrams for TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/commutative-diagrams
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/commutative-diagrams.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/commutative-diagrams.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a TikZ library for making commutative
diagrams easy to design, parse and tweak.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/plain/commutative-diagrams
%{_texmfdistdir}/tex/latex/commutative-diagrams
%{_texmfdistdir}/tex/generic/commutative-diagrams
%{_texmfdistdir}/tex/context/third/commutative-diagrams
%doc %{_texmfdistdir}/doc/generic/commutative-diagrams

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
