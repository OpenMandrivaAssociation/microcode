Summary:   Intel P6 / AMD CPU Microcode 
Name:      microcode
Version:   0.20100204
Release:   %mkrel 1
Group:     System/Kernel and hardware
License:   Distributable
# use update-intel-microcode --download-only (from microcode_ctl) to update
Source0:   intel-microcode.dat
# use update-amdl-microcode --download-only (from microcode_ctl) to update
Source1:   amd-ucode-latest.tar
Buildroot: %_tmppath/%name-%version-buildroot
ExclusiveArch: %ix86 x86_64

%description
Since PentiumPro, Intel CPU are made of a RISC chip and of a microcode whose
purpose is to decompose "old" ia32 instruction into new risc ones.
P6 familly is concerned: PPro, PII, Celeron, PIII, Celeron2.
Recent kernels have the ability to update this microcode.

The microcode update is volatile and needs to be uploaded on each system
boot. I.e. it doesn't reflash your cpu permanently.
Reboot and it reverts back to the old microcode.

This package contains microcode for Intel CPU, as well as microcode for 
AMD CPU (AMD Phenom(TM), AMD Opteron(TM) and AMD Turion(TM) 64 Ultra).

%prep
%setup -q -T -c

%build

%install
rm -rf $RPM_BUILD_ROOT 

mkdir -p $RPM_BUILD_ROOT%{_datadir}/misc
install -m644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/misc

mkdir -p $RPM_BUILD_ROOT/lib/firmware/amd-ucode 
tar xf %{SOURCE1} -C $RPM_BUILD_ROOT/lib/firmware/amd-ucode

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/lib/firmware/amd-ucode
%{_datadir}/misc/intel-microcode.dat

