# 1. Kiểm tra phiên bản
Muốn nâng cấp, chuyển đổi phiên bản, cần kiểm tra phiên bản hiện tại (chạy __winver__) và kiểm tra theo lệnh dưới đây. Chạy CMD quyền administrator rồi chạy các lệnh:
```bash
 % Kiểm tra phiên bản hiện tại:
 slmgr -dli
 Dism /Online /Get-CurrentEdition
  
 % Kiểm tra phiên bản có thể nâng cấp lên:
 Dism /Online /Get-TargetEditions
```
Nếu phiên bản win10 2015 có thể nâng cấp lên win10 2020 theo cách bên dưới, để chuyển đổi loại win

Để đổi key từ CMD có thể chạy lệnh:
```Changepk.exe /productkey:xxxxx-xxxxx-xxxxx-xxxxx-xxxxx```

# 2. Update windows 10 lên bản mới nhất 
Tải về bản update trên trang chủ tại đây: 
[https://www.microsoft.com/en-gb/software-download/windows10](https://www.microsoft.com/en-gb/software-download/windows10)

# 3. Cách active window và office

Get ConfirmationID (step3) transmission of Windows operating systems and Office versions for Windows / Office activation.

## Step 1: Open CMD with administrator privileges (Run as administrator).

## Chuyển đổi office 2019 Retail sang VL
Chạy đoạn code này trong CMD admin

```bash

reg Delete HKLM\Software\Wow6432Node\Microsoft\Office\16.0\Common\OEM /f
reg Delete HKLM\Software\Microsoft\Office\16.0\Common\OEM /f
cscript slmgr.vbs /upk 70d9ceb6-6dfa-4da4-b413-18c1c3c76e2e
cscript slmgr.vbs /upk de52bd50-9564-4adc-8fcb-a345c17f84f9
cscript slmgr.vbs /upk 84832881-46ef-4124-8abc-eb493cdcf78e
cscript slmgr.vbs /upk 52c4d79f-6e1a-45b7-b479-36b666e0a2f8
cscript slmgr.vbs /upk 5f472f1e-eb0a-4170-98e2-fb9e7f6ff535
cscript slmgr.vbs /upk a3072b8f-adcc-4e75-8d 62-fdeb9 bdfae57
cscript slmgr.vbs /upk 70d9ceb6-6dfa-4da4-b413-18c1c3c76e2e
if exist "%ProgramFiles%\Microsoft Office\Office16\ospp.vbs" cd /d "%ProgramFiles%\Microsoft Office\Office16"
if exist "%ProgramFiles(x86)%\Microsoft Office\Office16\ospp.vbs" cd /d "%ProgramFiles(x86)%\Microsoft Office\Office16"
cscript ospp.vbs /remhst
cscript ospp.vbs /ckms-domain
for /f %i in ('dir /b ..\root\Licenses16\ProPlus2019VL_MAK*.xrm-ms') do cscript ospp.vbs /inslic:"..\root\Licenses16\%i"
cscript //nologo ospp.vbs /inpkey:TNJMC-468RB-B4QTR-W32BX-BKP63
cscript //nologo ospp.vbs /act
cscript //nologo ospp.vbs /dinstid > step2.txt
start step2.txt
cls
cscript ospp.vbs /actcid:
```


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
Khi nhận được mã CID, nhập theo cách sau:
cái này ngay trong chỗ lấy CID nó có luôn, chỉ việc copy vào chạy

```bash
cscript.exe "%windir%\system32\slmgr.vbs" /atp <<<CID>>>
cscript.exe "%windir%\system32\slmgr.vbs" /ato
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

# Check license

```bash
for %a in (4,5,6) do (if exist "%ProgramFiles%\Microsoft Office\Office1%a\ospp.vbs" (cd /d "%ProgramFiles%\Microsoft Office\Office1%a")
if exist "%ProgramFiles(x86)%\Microsoft Office\Office1%a\ospp.vbs" (cd /d "%ProgramFiles(x86)%\Microsoft Office\Office1%a"))&cls
cls
cscript ospp.vbs /dstatus
echo
```
