# Upload file and some other fields to PHP server

## Phương pháp 1:


Python:

```python
import requests 
CompanyName='TA'
URL = "https://aisolutions.vn/apps/auto_booking/getdata.php"
data = {'dir':CompanyName, 'security':'RSA'}
files = {'file':('Data.txt', open('Data.txt', 'rb'))}
r = requests.post(URL, data=data, files=files)
# print(r.content)
```

PHP:

```PHP
<?php
date_default_timezone_set("Asia/Ho_Chi_Minh");
$target_dir = "uploads/".$_POST['dir'].'/';
if (!file_exists($target_dir)) {
    mkdir($target_dir, 0777, true);
}

$target_file = $target_dir . $_FILES["file"]["name"].'__'.date('Y-m-d__H-m-s').'.txt';;
move_uploaded_file($_FILES["file"]["tmp_name"], $target_file);
echo("Done uploading");
?>
```


## Phương pháp 2:

Python:

```python 
import urllib
mydata=[('one','1'),('two','2')]     
url='http://localhost/test/getdata.php'   
data = urllib.parse.urlencode(mydata).encode("utf-8")
req = urllib.request.Request(url)
with urllib.request.urlopen(req,data=data) as f:
    resp = f.read()
    print(resp)
```
PHP:

```PHP
<?php
date_default_timezone_set("Asia/Ho_Chi_Minh");
echo "one=".$_POST['one'];
echo "two=".$_POST['two'];
echo ";";
?>
```

