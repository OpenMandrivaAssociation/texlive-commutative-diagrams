%global tl_name commutative-diagrams
%global tl_revision 71053

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.2
Release:	%{tl_revision}.1
Summary:	CoDi: Commutative Diagrams for TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/commutative-diagrams
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/commutative-diagrams.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/commutative-diagrams.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a TikZ library for making commutative diagrams
easy to design, parse and tweak.

