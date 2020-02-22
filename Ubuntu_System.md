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

# Ubuntu compress, zip, unzip files with progress:

https://www.cyberciti.biz/howto/question/general/compress-file-unix-linux-cheat-sheet.php

## Compressing files

```bash
gzip {filename}
	gzip mydata.doc
	gzip *.jpg
	ls -l

bzip2 {filename}
	bzip2 mydata.doc
	bzip2 *.jpg
	ls -l

zip {.zip-filename} {filename-to-compress}
	zip mydata.zip mydata.doc
	zip data.zip *.doc
	ls -l

tar -zcvf {.tgz-file} {files}
tar -jcvf {.tbz2-file} {files}
	tar -zcvf data.tgz *.doc
	tar -zcvf pics.tar.gz *.jpg *.png
	tar -jcvf data.tbz2 *.doc
	ls -l
```

## Decompressing files:

```bash
gzip -d {.gz file}
gunzip {.gz file}
	gzip -d mydata.doc.gz
	gunzip mydata.doc.gz

bzip2 -d {.bz2-file}
bunzip2 {.bz2-file}
	bzip2 -d mydata.doc.bz2
	gunzip mydata.doc.bz2

unzip {.zip file}
	unzip file.zip
	unzip data.zip resume.doc
!unzip -o thch30_train_dev_test.zip -d /. | pv -l >/dev/null

tar -zxvf {.tgz-file}
tar -jxvf {.tbz2-file}
	tar -zxvf data.tgz
	tar -zxvf pics.tar.gz *.jpg
	tar -jxvf data.tbz2
```

## How to unzip files bigger than 4GB?

```bash
sudo apt-get install p7zip-full
7z x huge.zip
```

# Copy file in Ubuntu with progress:

```
sudo apt-get install pv
pv my_big_file > backup/my_big_file
```
Dùng rsync:

```
$ rsync -ah --progress source-file destination-file
sending incremental file list
source-file
        621.22M  57%  283.86MB/s    0:00:01
```

You can copy a file to your media by entering
```
sudo apt-get install gcp
gcp /home/mike/file.mp4 /media/usb

gcp ~/Videos_incIplayer/mars.flv /media/Mik2
Copying 168.57 MiB 100% |####################################|   7.98 M/s Time: 00:00:22

curl -o destination FILE://source

cp -rv old-directory new-directory

sudo apt-get install progress
cp bigfile newfile & progress -mp $!
    output: [11471] cp /media/Backup/Downloads/FILENAME.file 
                    29.9% (24.2 MiB / 16 MiB)

```

