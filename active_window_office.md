
# Cách active window và office
Get ConfirmationID (step3) transmission of Windows operating systems and Office versions for Windows / Office activation.

## Step 1: Open CMD with administrator privileges (Run as administrator).

## Step 2A: Active Windows Chạy lệnh sau:

(thay [your_product_key] bằng key của mình)

```bash
cd %windir%\system32
set k1=[your_product_key]
cls
cscript slmgr.vbs /rilc
cscript slmgr.vbs /upk
cscript slmgr.vbs /ckms
cscript slmgr.vbs /cpky
sc config Winmgmt start=demand & net start Winmgmt
sc config LicenseManager start=auto & net start LicenseManager
sc config wuauserv start=auto & sc start wuauserv
@echo on&mode con: cols=20 lines=2
cscript slmgr.vbs /ipk %k1%
@mode con: cols=100 lines=30
cscript slmgr.vbs /dti>C:\IID.txt
cscript slmgr.vbs /dti>C:\IID.txt
start C:\IID.txt
echo
```

## Step 2B: Active Office Chạy lệnh sau:

```bash
for %a in (4,5,6) do (if exist "%ProgramFiles%\Microsoft Office\Office1%a\ospp.vbs" (cd /d "%ProgramFiles%\Microsoft Office\Office1%a")
if exist "%ProgramFiles(x86)%\Microsoft Office\Office1%a\ospp.vbs" (cd /d "%ProgramFiles(x86)%\Microsoft Office\Office1%a"))&cls
set k1=[your_product_key]
cls
cscript ospp.vbs /inpkey:%k1%
cscript ospp.vbs /dinstid>id.txt
start id.txt
echo
```

## Step 3: Get InstallationID (step2) in IID.txt  
## Step 4: Nhập CID vào

After obtaining the ConfirmationID (step3), select the version that matches the current version and click to get the CMD command then paste into CMD to complete activation of Windows / Office.
