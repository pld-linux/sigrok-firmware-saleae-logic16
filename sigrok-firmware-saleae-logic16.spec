Summary:	Firmware for Saleae Logic16 logic analyzer
Name:		sigrok-firmware-saleae-logic16
Version:	1.1.15
Release:	1
License:	Unknown
Group:		Applications/Engineering
URL:		http://sigrok.org/wiki/Saleae_Logic16
Source0:	http://downloads.saleae.com/Logic%20%{version}%20(64-bit).zip
# NoSource0-md5:	6d91d1decac041dc29405379af530261
NoSource:	0
Source1:	http://sigrok.org/gitweb/?p=sigrok-util.git;a=blob_plain;f=firmware/saleae-logic16/sigrok-fwextract-saleae-logic16;hb=HEAD;/sigrok-fwextract-saleae-logic16
# Source1-md5:	c69f130ea7f4ac86219737ad4f6b9dc0
Source2:	http://sigrok.org/gitweb/?p=sigrok-util.git;a=blob_plain;f=firmware/saleae-logic16/parseelf.py;hb=HEAD;/parseelf.py
# Source2-md5:	ee0323c709a7cc8828f4806988b45e85
BuildRequires:	python3
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firmware for The Saleae Logic16 - a USB-based, 16-channel logic
analyzer with 100/50/32/16MHz sampling rate (at 3/6/9/16 enabled
channels).

%prep
%setup -q -n "Logic %{version} (64-bit)"
install %{SOURCE1} sigrok-fwextract-saleae-logic16
install %{SOURCE2} parseelf.py

%build
python3 sigrok-fwextract-saleae-logic16 Logic

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/sigrok-firmware

install saleae-logic16-fx2.fw saleae-logic16-fpga-18.bitstream saleae-logic16-fpga-33.bitstream \
	$RPM_BUILD_ROOT%{_datadir}/sigrok-firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/sigrok-firmware/saleae-logic16-fx2.fw
%{_datadir}/sigrok-firmware/saleae-logic16-fpga-18.bitstream
%{_datadir}/sigrok-firmware/saleae-logic16-fpga-33.bitstream
