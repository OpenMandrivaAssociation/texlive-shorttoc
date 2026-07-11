%global tl_name shorttoc
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Table of contents with different depths
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/shorttoc
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/shorttoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/shorttoc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/shorttoc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package to create another table of contents with a different depth,
useful in large documents where a detailed table of contents should be
accompanied by a shorter one, giving only a general overview of the main
topics in the document.

