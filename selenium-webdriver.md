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

# Chờ cho đến khi load trang

```python
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://pythonbasics.org')
timeout = 3
try:
    element_present = EC.presence_of_element_located((By.ID, 'main'))
    #element_present = EC.presence_of_element_located((By.CLASS_NAME, 'btn')) #By.ID
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")
 ```


