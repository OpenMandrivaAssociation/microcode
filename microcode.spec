Summary:	Intel P6 CPU Microcode 
Name:		microcode
Version:	0.20140323
Release:	3
Group:		System/Kernel and hardware
License:	Distributable
# use update-intel-microcode --download-only (from microcode_ctl) to update
Source0:	intel-microcode.dat
# AMD microcode comes from kernel-firmware-extra these days.
BuildArch: noarch

%description
Since PentiumPro, Intel CPU are made of a RISC chip and of a microcode whose
purpose is to decompose "old" ia32 instruction into new risc ones.
P6 familly is concerned: PPro, PII, Celeron, PIII, Celeron2.
Recent kernels have the ability to update this microcode.

The microcode update is volatile and needs to be uploaded on each system
boot. I.e. it doesn't reflash your cpu permanently.
Reboot and it reverts back to the old microcode.

This package contains microcode for Intel CPU.

Microcode updates for AMD CPUs can be found in the
kernel-firmware-extra package.

%prep
%setup -q -T -c

%build

%install 

mkdir -p %{buildroot}/lib/firmware/intel-microcode
install -m644 %{SOURCE0} %{buildroot}/lib/firmware/intel-microcode

%files
%defattr(-,root,root,-)
/lib/firmware/intel-microcode/intel-microcode.dat

