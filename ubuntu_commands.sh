# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# remove a dir with contents:
rm -fdr <dir_name>
uses: rm -fdr All_database_processed/
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
nvidia-smi
---------------------------
nvidia-smi --format=csv --query-gpu=temperature.gpu,fan.speed,pstate,power.draw,clocks.current.graphics
nvidia-smi --format=csv,noheader --query-gpu=temperature.gpu,fan.speed,pstate,power.draw,clocks.current.graphics
nvidia-smi --format=csv --query-gpu=index,name,temperature.gpu,fan.speed,pstate,power.draw,clocks.current.graphics

Output: 0, GeForce GTX 1080 Ti, 78, 46 %, P2, 178.71 W, 1797 MHz
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
Find files or folders in Ubuntu:
- find -name "\*ASR\*" : find all file/dir name include ASR
- find -typy d -name "\*ASR\*" : find all *dir* name include ASR
- find -type f -name "*libcudart*"   : find all files libcudart.so.* in current folder
- find -type f -name "*libcudnn.so*"   : find all files libcudnn.so.*

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
List Physical Hardisk in Ubuntu:
- sudo lshw -class disk -short
Results:
H/W path               Device           Class          Description
==================================================================
/0/100/14/1/5/0.0.0    /dev/sdd         disk           1TB Elements 10A8
/0/1/0.0.0             /dev/sda         disk           256GB Reeinno CY256GB
/0/2/0.0.0             /dev/sdb         disk           1TB WDC WD10EZEX-08Y
/0/3/0.0.0             /dev/sdc         disk           1TB ST31000528AS
- sudo lsblk -o NAME,FSTYPE,SIZE,MOUNTPOINT,LABEL

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
PYTHON - AUTO GENERATE REQUIREMENTS.TXT:
    Method 1:
      * pip freeze > requirements.txt   
      
    Method 2:
      * pip install pipreqs
      * pipreqs /path/to/project
    (to install: pip install -r requirements.txt)      

##############################################################
Anaconda GUI in ubuntu
##############################################################
- Install anaconda for ubuntu
- do this:
    step 1 : $ conda install -c anaconda anaconda-navigator​
    step 2 : $ anaconda-navigator
- Or do this:
    $ source ~/anaconda3/bin/activate root
    $ anaconda-navigator
source: https://stackoverflow.com/questions/43030871/anaconda-navigator-ubuntu16-04

##############################################################
Login to jupyter server from local machine
##############################################################
server side:#TODO
if want to run forever, run TMUX first
1. activate Anaconda:
TMUX
conda info --envs
source activate P3

2. Active jupyter:
jupyter notebook --no-browser --port=[XXXX]
eg:
input: 1233 is the unique port number
__ jupyter notebook --no-browser --port=1233 __

results if successful:
[I 15:17:34.760 NotebookApp] Serving notebooks from local directory: /home/tact/AudioDBs
[I 15:17:34.760 NotebookApp] 0 active kernels
[I 15:17:34.760 NotebookApp] The Jupyter Notebook is running at:
[I 15:17:34.760 NotebookApp] http://localhost:1233/?token=cecfec85f6c1cb65de4ae9f9feb84ee2318f497d095e40d7
[I 15:17:34.760 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 15:17:34.760 NotebookApp] 
    
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:1233/?token=cecfec85f6c1cb65de4ae9f9feb84ee2318f497d095e40d7
 -------------------------
 3. Client side:
 ssh -f [USER]@[SERVER] -L [YYYY]:localhost:[XXXX] -N
 
eg:
__ ssh -f tact@192.168.0.6 -L 2344:localhost:1233 -N __
tact@192.168.0.6's password: 

4. Access from local browser:
http://localhost:2344

copy token above, paste into login input text then press *login*
 



##############################################################
Linux system: share folder / mount a remote dir to local
##############################################################
sshfs user@host:/home/user/project/summary_logs ~/summary_logs
VD: sshfs tact@192.168.0.6:/home/tact/AudioDBs/Olivia/logs ~/kr/logs
    ref:https://stackoverflow.com/questions/37987839/how-can-i-run-tensorboard-on-a-remote-server
    
sshfs ubuntu@ubun:/home/4T/ubuntu  /home/ubuntu/DBs
Share Folder: select folder then share as WINDOWS, then run: "chmod 777 -R <folder name>" to give All permission to all users
##############################################################
Linux system: Startup a program in ubuntu manualy
##############################################################
Copy/delete the application's .desktop file to/from ~/.config/autostart/
.desktop file usually located at /usr/share/applications but you can create a custom if you want.

-------------------------------------------------------
example: file: ~/.config/autostart/minergate.desktop
[Desktop Entry]
Type=Application
Hidden=false
Exec=/opt/minergate/minergate --auto
Name=Minergate
Terminal=false
-------------------------------------------------------
to run any command before login as root add it to: /etc/rc.local
to run any command after  login as user add it to: ~/.bash_profile, contrary to ~/.bashrc



##############################################################
Linux system: Access root ssh from ssh
##############################################################
nano /etc/ssh/sshd_config 
change to like this:
    # Authentication:
    LoginGraceTime 120
    #PermitRootLogin prohibit-password
    PermitRootLogin yes
    StrictModes yes
saved!    
root@u1080:~# service ssh restart
root@u1080:~# service sshd restart


##############################################################
Linux system: install code editor geany, better than gedit: code folding, show indent guide, show space,...
##############################################################
download this:
to get hightlight words when double-click!
https://sourceforge.net/projects/geanyhighlightselectedword/files/latest/download
Open INSTALL file to read it, instructions to install in there:
  $ cd ~/SourcesOfGeanyHighlightSelectedWordPlugin                           
  $ bash installThesePackagesFirst.sh                                        
  $ bash buildGeanyFromSources.sh   ### Open this file, change version to latest version before run.                                         
  $ make all                                                                 
  $ make deploy                                                              

Other method:
   $ sudo apt-get install geany
   $ sudo apt-get install geany-plugins
or build from source from: https://www.geany.org/Download/Releases
   $ ./configure
   $ make
   $ make install

if already install, we do like this:
    $ su root
    $ which geany       ## /usr/local/bin/geany
    $ mv geany geany0   # rename old file
    $ cp   /home/ubu/src/src_geany-1.33/usr/bin/geany    /usr/local/bin # change version


##############################################################
Tmux: 
##############################################################
Attact window:
  $ tmux at -t 0

Scroll screen:
  $ set -g mouse on        #For tmux version 2.1 and up
  ctr_b, PgUp  or ctr_b,[


##############################################################
Ubuntu SSH without password: How to automate SSH login with password?
##############################################################
# ssh-keygen
# ssh-copy-id ubuntu@10.1.58.20
# ssh    'ubuntu@10.1.58.20'
# ssh -Y 'ubuntu@10.1.58.20'  
# -Y: lai moi dau ra sang may local, vd: chay firfox tren terminal ssh nhung no lai hien thi tren local

ServerAdd='tact@10.1.58.23' # 1080ti
ssh-keygen
ssh-copy-id $ServerAdd
ssh -Y $ServerAdd

ServerAdd='ubuntu@10.1.58.20' # titanXP

https://askubuntu.com/questions/46930/how-can-i-set-up-password-less-ssh-login

copy file in ubuntu: use ssh:
scp .ssh/id_rsa1080.pub tact@10.1.58.23:/home/tact/.ssh


##############################################################
Ubuntu: Run ipython notebook with browser from local to server ubuntu:
##############################################################
Server side:
ipython notebook --no-browser --ip=* --port=8889

#-------------------------------------------------------------------------------------------------
results:
(P3)tact@u1080:~$ ipython notebook --no-browser --ip=* --port=8889
[TerminalIPythonApp] WARNING | Subcommand `ipython notebook` is deprecated and will be removed in future versions.
...........
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8893/?token=ce8e4ff801099d2ec0745dcdcc81007164983f79bf626a53
#-------------------------------------------------------------------------------------------------

Local side: 
http://10.1.53.4:8889/tree       (IP la IP cua may chu, dang chay ipython)
#-------------------------------------------------------------------------------------------------


##############################################################
ipython: ipython notebook width 100%
##############################################################
ref: https://gist.github.com/paulochf/f6c9ed0b39f85dd85270

from IPython.display import display, HTML

display(HTML(data="""
<style>
    div#notebook-container    { width: 95%; }
    div#menubar-container     { width: 65%; }
    div#maintoolbar-container { width: 99%; }
</style>
"""))
#-----------------------------------------------------------
nano ~/.jupyter/custom/custom.css
paste this:

.container {
    width: 99% !important;
}   
div.cell.selected {
    border-left-width: 1px !important;	
}
div.output_scroll {
    resize: vertical !important;
}
#-----------------------------------------------------------
nano ~/.ipython/profile_default/static/custom/custom.css
paste this into:
    .container { width:100% !important; }


##############################################################
Ubuntu: Create bootable install OS disk (ubuntu/window/...system):
##############################################################
1. unplug USB:
    ls /dev/sd*
    
/dev/sda   /dev/sda2  /dev/sdb   /dev/sdb2  /dev/sdc1  
/dev/sda1  /dev/sda5  /dev/sdb1  /dev/sdc   

2. Plug USB into ubuntu machine:
    ls /dev/sd*
    /dev/sda   /dev/sda2  /dev/sdb   /dev/sdb2  /dev/sdc1  /dev/sdd1 <------
    /dev/sda1  /dev/sda5  /dev/sdb1  /dev/sdc   /dev/sdd    <------
    
2.1. see different disk:
    /dev/sdd /dev/sdd1

3. Navigate to the location of your source ISO
4.  Run dd command to copy files from ISO to disk
    sudo  dd   if=ubuntu-17.10.1-desktop-amd64.iso    of=/dev/sdd    status=progress
    
    output:
    1432+1 records in
    1432+1 records out
    1502576640 bytes (1.5 GB, 1.4 GiB) copied, 0.567973 s, 2.6 GB/s

http://www.linuxandubuntu.com/home/how-to-burn-iso-image-to-dvd-and-usb-using-dd



##############################################################
Ubuntu: Install Sublime in linux:
##############################################################

sudo add-apt-repository ppa:webupd8team/sublime-text-3
sudo apt-get update 
sudo apt-get install sublime-text-installer
    Lisense key: try in here: tested and successful!
    http://appnee.com/sublime-text-3-universal-license-keys-collection-for-win-mac-linux/


##############################################################
Install Samba and Share file from linux to windows
##############################################################
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install samba samba-common system-config-samba python-glade2 -y
sudo apt install samba samba-common-bin
sudo systemctl start smbd
sudo systemctl start nmbd
sudo apt install system-config-samba
#If you get the following error:
#could not open configuration file `/etc/libuser.conf': No such file or directory
sudo touch /etc/libuser.conf
------
sudo adduser username
sudo smbpasswd -a username
----
sudo systemctl restart smbd nmbd
# Huonf dan rat chuan, hay, tested tren Ubuntu 18.04
# https://www.linuxbabe.com/ubuntu/system-config-samba-ubuntu-16-04


##############################################################
How to install pytorch in Anaconda with conda or pip?
##############################################################
conda create -n pytorch_env python=3.5
source activate pytorch_env
conda install -c soumith pytorch
python
> import torch

#https://stackoverflow.com/questions/49918479/how-to-install-pytorch-in-anaconda-with-conda-or-pip



##############################################################
Anaconda Jupyter Notebook: Change startup folder of notebook:
##############################################################
Use the jupyter notebook config file:

Open cmd (or Anaconda Prompt) and run jupyter notebook --generate-config.

This writes a file to C:\Users\username\.jupyter\jupyter_notebook_config.

Search for the following line: #c.NotebookApp.notebook_dir = ''

Replace by c.NotebookApp.notebook_dir = '/the/path/to/home/folder/'

Make sure you use forward slashes in your path and use /home/user/ instead of ~/ for your home directory,
https://stackoverflow.com/questions/35254852/how-to-change-the-jupyter-start-up-folder
ex:
File: C:\Users\ta\.jupyter\jupyter_notebook_config.py
Line: 214: c.NotebookApp.notebook_dir = 'j:/2018'

##############################################################
Anaconda Jupyter Notebook: Run Remote Notebook on server from local:
##############################################################
1. connect Xshell/ ssh to server.
2. Run On server: (example: 1080ti server)
    conda info --envs
    source activate tf
  ipython notebook --no-browser --ip=* --port=1234
  ipython notebook --no-browser --ip=0.0.0.0 --port=1234  
(port can be change)
result:
http://(ubu or 127.0.0.1):1234/?token=113fbcd684007d6a72f8839c94637951d613b136a39b040c

3. Run on local:
- copy that address, paste to local browser
- change IP address to real IP: http://10.1.53.1:1234/?token=113fbcd684007d6a72f8839c94637951d613b136a39b040c
- Enjoy!

##############################################################
Chạy trong Notebook, lấy thông tin của main, cpu
##############################################################
# !pip install torchvision
# !apt-get install lshw
# !lshw 
#----------------------------------------------
!cat /sys/devices/virtual/dmi/id/board_vendor 
!cat /sys/devices/virtual/dmi/id/board_name
!lspci
!lscpu




##############################################################
Add New sudo User ubuntu:
##############################################################
    sudo adduser u
    sudo adduser u sudo
    usermod -aG sudo u
    su - u


##############################################################
Change language in ssh of ubuntu to english
##############################################################

    sudoedit /etc/default/locale

    LANG="en_US"
    LANGUAGE="en_US:en"
    https://askubuntu.com/questions/133318/how-do-i-change-the-language-via-a-terminal    
or: 
    export LC_ALL=C
    https://askubuntu.com/questions/264283/switch-command-output-language-from-native-language-to-english

##############################################################
TensorBoard server client:
##############################################################
    Server:
        tensorboard --logdir=. --host=0.0.0.0 --port=6006
    Local: 
        http://10.1.53.1:6006


##############################################################
Python: install Pythable
##############################################################

def RunSudoCMD(cmd):
    import pexpect                          # here you issue the command with "sudo"
    child = pexpect.spawn(cmd) # it will prompt something like: "[sudo] password for < generic_user >:" # you "expect" to receive a string having "password"
    s=child.expect('password')              # if it's found, send the password
    s=child.sendline('123')                 # read the output:
    outp=str(child.read()).replace('\\r','').split('\\n')
    for s in outp[1:-1]:
        print(s)

# RunSudoCMD('sudo apt-get install libhdf5-serial-dev -y')
# !conda install -c anaconda c-blosc -y
# !pip install tables

##############################################################
ubuntu: FFMPEG Chia clip ra thành nhiều phần bằng nhau:
##############################################################

ffmpeg -i input.avi -c copy -map 0 -segment_time 00:10:00 -f segment -reset_timestamps 1 Output_%03d.avi

https://unix.stackexchange.com/a/212518















