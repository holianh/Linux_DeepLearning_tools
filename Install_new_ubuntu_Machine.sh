sudo apt update  -y
sudo apt upgrade  -y
sudo apt-get dist-upgrade  -y
sudo apt-get install ubuntu-restricted-extras  -y
sudo apt install gnome-tweak-tool  -y
sudo apt-get install gdebi  -y
sudo apt-get install synaptic -y
sudo apt-get install vlc -y
sudo apt-get filezilla -y
sudo apt-get install shutter -y
sudo apt install gdebi-core  -y
#wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#sudo gdebi google-chrome-stable_current_amd64.deb  -y
sudo apt-get install redshift redshift-gtk  -y
sudo apt install snapd   -y Install Shotcut Video Editor in Linux  -y
sudo snap install shotcut --classic   -y

# @@@ go and install: https://code.visualstudio.com/

# @@@ Peek – A Simple Animated Gif Screen Recorder for Linux:
sudo add-apt-repository ppa:peek-developers/stable 
sudo apt-get update   -y
sudo apt-get install peek   -y

# @@@GitBook Editor: https://www.fossmint.com/gitbook-editor-a-git-workflow-from-your-linux-desktop/

# @@@Whatever – A Lightweight Evernote Client for Linux
# @@@ https://sourceforge.net/projects/whatever-evernote-client/files/v1.0.0/

# @@@ MOC – The Best Music Player for Your Linux Console
sudo apt-get install moc moc-ffmpeg-plugin   -y

# @@@  Stacer – The Linux System Optimizer You’ve Been Waiting For: stacer_1.0.9_amd64.deb
#wget https://github.com/oguzhaninan/Stacer/releases/download/v1.0.4/Stacer_1.0.4_amd64.deb
#sudo dpkg --install Stacer_1.0.4_amd64.deb    
#Stacer

########################################################1
Server=0
echo "Install APP"
 
echo "apt-get htop ..."   & sudo apt-get install htop
echo "apt-get ncdu ..."   & sudo apt-get install ncdu
echo "apt-get geany ..."  & sudo apt-get install geany -y
echo "geany-plugins ..."  & sudo apt-get install geany-plugins -y
echo "tmux ..."           & sudo apt-get install tmux -y

sudo add-apt-repository ppa:mc3man/trusty-media
echo "apt-get update ..." & sudo apt-get update
 
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

########################################################2
if [$Server == 1]; then #1
	echo "ubuntu-desktop ..." & sudo apt-get install  -y --no-install-recommends ubuntu-desktop gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal
	echo "gnome-pane     ..." & sudo apt-get install  -y gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal
	echo "install ffmpeg ..." & sudo apt-get install  -y gnome-core xfce4 firefox nano -y --force-yes
fi #1

########################################################3
echo "libav-tools    ..." & sudo apt-get install  -y libav-tools
echo "build-essentia ..." & sudo apt-get install  -y build-essential git libatlas-base-dev libopencv-dev
echo "libblas-dev    ..." & sudo apt-get install  -y libblas-dev liblapack-dev
echo "nvidia-cuda-toolkit ..." & sudo apt-get install  -y nvidia-cuda-toolkit
#sudo apt-get install  -y wine

########################################################4
if [$Server == 1]; then #2
	echo "Config login root user"
	sudo sed -i 's/prohibit-password/yes/' /etc/ssh/sshd_config
	sudo sed -i 's/#PermitRootLogin/PermitRootLogin/' /etc/ssh/sshd_config
fi #2

########################################################5
echo "Install Anaconda: CD to Anaconda path" 
bash Anaconda3-5.2.0-Linux-x86_64.sh 
PATH=/home/u/anaconda3/bin:$PATH
sudo apt install nvidia-340      
sudo apt install nvidia-utils-390

conda install -c anaconda anaconda-navigator -y
conda create -n P3 python=3.6 -y
source activate P3
conda install tensorflow-gpu -y
conda install keras-gpu -y
pip install pydub -y

source deactivate
########################################################6
if [$Server == 1]; then
	echo "Install vncserver"
	apt update && apt install xfce4 xfce4-goodies tightvncserver
	vncserver
	vncserver -kill :1
	vncserver -kill :2
fi
echo ""
echo ""
echo "Manual do: install Dconf in software to Enable [Click to minimize windows]"

########################################################7
sudo dpkg –add-architecture i386
sudo apt install wine64
sudo apt-get install cups-pdf -y # print to PDF

#samba:
# sudo system-config-samba


# Install photo Editor:
#install Pinta
sudo apt-get install pinta
#install GIMP
# Uninstall GIMP:
#sudo apt-get autoremove gimp gimp-plugin-registry
sudo add-apt-repository ppa:otto-kesselgulasch/gimp
sudo apt-get update
sudo apt-get install gimp
#wechat
sudo apt install snapd snapd-xdg-open -y
sudo snap install electronic-wechat
#run: electronic-chat




########################################################8
# END AUTO RUN
########################################################9
