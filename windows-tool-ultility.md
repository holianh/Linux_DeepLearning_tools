# Hiển thị pass wifi trên máy tính

```
netsh wlan show profile 
netsh wlan export profile folder=c:\ key=clear
```

# Thêm command vào menu chuột phải desktop

Mở registry (CMD>regedit). Vào `Computer\HKEY_CLASSES_ROOT\Directory\Background\shell` thêm key muốn tạo, rồi thêm key Command, vd:
`Computer\HKEY_CLASSES_ROOT\Directory\Background\shell\TA-Open Word\Command`, bên phải của Command, chỗ (Default), value dán đường dẫn file cần chạy vào là dc.












