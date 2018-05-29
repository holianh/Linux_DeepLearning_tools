
########################################################
echo "Install APP"
 
echo "apt-get htop ..."   & sudo apt-get install htop
echo "apt-get ncdu ..."   & sudo apt-get install ncdu
echo "apt-get geany ..."  & sudo apt-get install geany -y
echo "geany-plugins ..."  & sudo apt-get install geany-plugins -y
echo "tmux ..."           & sudo apt-get install tmux -y

sudo add-apt-repository ppa:mc3man/trusty-media
echo "apt-get update ..." & sudo apt-get update
echo "dist-upgrade   ..." & sudo apt-get dist-upgrade
echo "install ffmpeg ..." & sudo apt-get install  -y ffmpeg
echo "install tree   ..." & sudo apt-get install  -y tree
echo "openssh-client ..." & sudo apt-get install  -y openssh-client
echo "openssh-server ..." & sudo apt-get install  -y openssh-server
echo "install sshpass..." & sudo apt-get install  -y sshpass
echo "install samba  ..." & sudo apt-get install  -y samba
echo "install vsftpd ftp" & sudo apt-get install  -y vsftpd ftp
echo "ibus-sunpinyin ..." & sudo apt-get install  -y ibus-sunpinyin
echo "exfat-fuse     ..." & sudo apt-get install  -y exfat-fuse exfat-utils
echo "ttf-mscorefonts..." & sudo apt-get install  -y ttf-mscorefonts-installer
echo "inst lm-sensors..." & sudo apt-get install  -y lm-sensors
echo "install psensor..." & sudo apt-get install  -y psensor
echo "install vnc4ser..." & sudo apt-get install  -y vnc4server
echo "ubuntu-desktop ..." & sudo apt-get install  -y --no-install-recommends ubuntu-desktop gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal
echo "gnome-pane     ..." & sudo apt-get install  -y gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal
echo "install ffmpeg ..." & sudo apt-get install  -y gnome-core xfce4 firefox nano -y --force-yes

echo "libav-tools    ..." & sudo apt-get install  -y libav-tools
echo "build-essentia ..." & sudo apt-get install  -y build-essential git libatlas-base-dev libopencv-dev
echo "libblas-dev    ..." & sudo apt-get install  -y libblas-dev liblapack-dev
echo "nvidia-cuda-toolkit ..." & sudo apt-get install  -y nvidia-cuda-toolkit
#sudo apt-get install  -y wine
########################################################
echo "Config login root user"
sudo sed -i 's/prohibit-password/yes/' /etc/ssh/sshd_config
sudo sed -i 's/#PermitRootLogin/PermitRootLogin/' /etc/ssh/sshd_config

########################################################
echo "Install Anaconda: CD to Anaconda path" 
bash Anaconda3-4.3.0-Linux-x86_64.sh 
PATH=/home/u/anaconda3/bin:$PATH

########################################################
echo "Install vncserver"
apt update && apt install xfce4 xfce4-goodies tightvncserver
vncserver
vncserver -kill :1
vncserver -kill :2
########################################################
########################################################
# END AUTO RUN
########################################################

#MANUAL.......





nano ~/.vnc/xstartup
    # Delete exists content, paste this:
    #-----------------------------------
    #!/bin/bash
    xrdb $HOME/.Xresources
    startxfce4 &
    #-----------------------------------
    #==> save exit
    
chmod +x ~/.vnc/xstartup
sudo nano /etc/systemd/system/vncserver@.service
    #paste this:
    [Unit]
    Description=Start TightVNC server at startup
    After=syslog.target network.target

    [Service]
    Type=forking
    User=USER
    PAMName=login
    PIDFile=/home/USER/.vnc/%H:%i.pid
    ExecStartPre=-/usr/bin/vncserver -kill :%i > /dev/null 2>&1
    ExecStart=/usr/bin/vncserver -depth 24 -geometry 1280x800 -localhost :%i
    ExecStop=/usr/bin/vncserver -kill :%i

    [Install]
    WantedBy=multi-user.target
    # save exit
    
systemctl daemon-reload
systemctl enable vncserver@1.service
systemctl start vncserver@1
## https://ubuntuwiki.com/2017/07/how-to-install-vnc-on-ubuntu-17-04/
########################################################

# may khach:
ssh-keygen
ssh-copy-id      u@10.1.53.13
ssh              u@10.1.58.20









































    
