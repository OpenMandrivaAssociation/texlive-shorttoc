# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/shorttoc
# catalog-date 2006-11-06 12:20:58 +0100
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-shorttoc
Version:	1.3
Release:	1
Summary:	Table of contents with different depths
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/shorttoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shorttoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shorttoc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shorttoc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A package to create another table of contents with a different
depth, useful in large documents where a detailed table of
contents should be accompanied by a shorter one, giving only a
general overview of the main topics in the document.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/shorttoc/shorttoc.sty
%doc %{_texmfdistdir}/doc/latex/shorttoc/00readme
%doc %{_texmfdistdir}/doc/latex/shorttoc/shorttoc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/shorttoc/shorttoc.dtx
%doc %{_texmfdistdir}/source/latex/shorttoc/shorttoc.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
