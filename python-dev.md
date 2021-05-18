# Auto Python to exe

Để biên dịch python sang exe, cần làm:

Nguồn: https://github.com/brentvollebregt/auto-py-to-exe

1. Cài đặt:

```bash
cách 1:
$ pip install auto-py-to-exe

Cách 2: cài từ nguồn:
$ git clone https://github.com/brentvollebregt/auto-py-to-exe.git
$ cd auto-py-to-exe
$ python setup.py install

Cách 3: Không cần cài, chạy theo local code:
$ git clone https://github.com/brentvollebregt/auto-py-to-exe.git
$ cd auto-py-to-exe
$ python -m pip install -r requirements.txt

Run:
- python -m auto_py_to_exe
- python run.py
```

Chú ý: môi trường chạy file run.py chính là môi trường đã chạy code, vì nó sẽ copy thư viện vào exe, nên nếu chạy trong môi trường khác, thì lúc chạy file exe tạo ra sẽ không chạy được.

2. Cấu hình

Khi chạy lệnh `python run.py` thì auto-python-to-exe sẽ hiển thị lên một sửa sổ, chú ý trong `setting` có mục output directory, đặt lại cho đúng.

