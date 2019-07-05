# Install Vivaldi:
https://vivaldi.com

cấu hình import, export password:

```
set==> enable:
vivaldi://flags/#PasswordImport
chrome://flags/#PasswordExport
```

Restart Vivaldi rồi vào đây để import/export:
vivaldi://settings/passwords

# Tạo shortcut key cho một script trong ubuntu
## tạo phím tắt cho "Open terminal here"
Create a script called Terminal (yes, without a extension) inside the folder ~/.local/share/nautilus/scripts with the following content:

```bash
# !/bin/sh
gnome-terminal
```

Make it executable, then close any Nautilus instance:

    ```bash
    chmod +x Terminal
    nautilus -q
    ```
    
Create (or edit) the ~/.config/nautilus/scripts-accels file adding these lines:

    ```bash
    F12 Terminal
    ; Commented lines must have a space after the semicolon
    ; Examples of other key combinations:
    ; <Control>F12 Terminal
    ; <Alt>F12 Terminal
    ; <Shift>F12 Terminal
    ```
    
Test it! Open Nautilus, right click, and choose Scripts > Terminal. Or, use the keyboard shortcut that you've just configured :)

