# Update windows 10 lên bản mới nhất 
Tải về bản update trên trang chủ tại đây: 
[https://www.microsoft.com/en-gb/software-download/windows10](https://www.microsoft.com/en-gb/software-download/windows10)

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