# Đăng nhập google bằng cookie vào selenium Chrome
Khi dùng Chrome, tạo một thư mục cookie tên là `selenium` chẳng hạn, rồi copy thư mục `%LOCALAPPDATA%\Google\Chrome\User Data` vào đó. 
[Xem chi tiết ở đây](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/docs/user_data_dir.md)

Trong code chạy như này:

```python
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=selenium")  # thư mục copy như trên
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get("www.google.com")
driver.get( mURL) #   taURL)#  
```


