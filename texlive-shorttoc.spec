Name:		texlive-shorttoc
Version:	15878
Release:	2
Summary:	Table of contents with different depths
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/shorttoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shorttoc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shorttoc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shorttoc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package to create another table of contents with a different
depth, useful in large documents where a detailed table of
contents should be accompanied by a shorter one, giving only a
general overview of the main topics in the document.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/shorttoc/shorttoc.sty
%doc %{_texmfdistdir}/doc/latex/shorttoc/00readme
%doc %{_texmfdistdir}/doc/latex/shorttoc/shorttoc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/shorttoc/shorttoc.dtx
%doc %{_texmfdistdir}/source/latex/shorttoc/shorttoc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
