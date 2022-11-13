Name:		texlive-thumby
Version:	16736
Release:	1
Summary:	Create thumb indexes for printed books
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/thumby
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thumby.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thumby.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package can generate thumb indexes for your document. It
features printing thumb indexes on one- or two-sided pages,
along with background- and foreground-color selection and full
LaTeX styling of the chapter numbers in the thumb indexes. The
height of each thumb index is automatically chosen based on the
number of chapters in your document, while the width is chosen
by the user. The package is designed to work with the memoir
class, and also requires PerlTeX and tikz/.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/thumby/thumby.sty
%doc %{_texmfdistdir}/doc/latex/thumby/LICENSE
%doc %{_texmfdistdir}/doc/latex/thumby/README
%doc %{_texmfdistdir}/doc/latex/thumby/example.pdf
%doc %{_texmfdistdir}/doc/latex/thumby/latexmkrc
%doc %{_texmfdistdir}/doc/latex/thumby/thumby.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
