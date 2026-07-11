%global tl_name thumby
%global tl_revision 16736

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Create thumb indexes for printed books
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thumby
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thumby.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thumby.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package can generate thumb indexes for your document. It features
printing thumb indexes on one- or two-sided pages, along with
background- and foreground-color selection and full LaTeX styling of the
chapter numbers in the thumb indexes. The height of each thumb index is
automatically chosen based on the number of chapters in your document,
while the width is chosen by the user. The package is designed to work
with the memoir class, and also requires PerlTeX and tikz/

