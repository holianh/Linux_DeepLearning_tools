#List youtube: https://goo.gl/7VKgdw

#1. Install NVIDIA Driver & CUDA 9.0/9.2 & CUDNN must be successull first.
#2. Install cuda 9.0(toolkit)
#3. Install cudnn7


install=0
if [ $install == 1 ]; then #1
  # Install  CUDNN: copy file cudnn to this dir.
  tar -xzvf cudnn-9.0-linux-x64-v7.1.tgz
  #Copy the following files into the CUDA Toolkit directory.
  sudo cp cuda/include/cudnn.h /usr/local/cuda/include
  sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
  sudo chmod a+r /usr/local/cuda/include/cudnn.h    /usr/local/cuda/lib64/libcudnn*
  #ref: http://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html
  #successful!
fi

# manual add by hand:
install=0
if [ $install == 1 ]; then #1
	sudo add-apt-repository ppa:peek-developers/stable 
	sudo add-apt-repository    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
		                       $(lsb_release -cs) \
		                       stable"
	sudo add-apt-repository ppa:mc3man/trusty-media
	sudo add-apt-repository ppa:otto-kesselgulasch/gimp
	sudo add-apt-repository ppa:obsproject/obs-studio
	sudo apt-add-repository ppa:fixnix/netspeed
#	sudo add-apt-repository ppa:ubuntu-vn/ppa
fi

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
sudo apt-get install ibus-unikey -y
ibus restart

# find string in file:
    sudo apt-get install regexxer -y 
    sudo apt-get install searchmonkey -y

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

echo "Install APP"
 
echo "apt-get htop ..."   & sudo apt-get install htop
echo "apt-get ncdu ..."   & sudo apt-get install ncdu
echo "apt-get geany ..."  & sudo apt-get install geany -y
echo "geany-plugins ..."  & sudo apt-get install geany-plugins -y
echo "tmux ..."           & sudo apt-get install tmux -y


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
########################################################

#Install Network indicator:
sudo apt-get install indicator-netspeed-unity


########################################################3
echo "libav-tools    ..." & sudo apt-get install  -y libav-tools
echo "build-essentia ..." & sudo apt-get install  -y build-essential git libatlas-base-dev libopencv-dev
echo "libblas-dev    ..." & sudo apt-get install  -y libblas-dev liblapack-dev
#~ echo "nvidia-cuda-toolkit ..." & sudo apt-get install  -y nvidia-cuda-toolkit
#sudo apt-get install  -y wine

########################################################
#~ Install Tensorboard=> config to use: "tensorboard" only at current dir, no need: tensorboard --logdir ############
pip install tensorboard -y
cd
locate tensorboard/program.py | xargs sed -i -e "s/logdir', ''/logdir', os.getcwd()/g" 
# ref: https://askubuntu.com/questions/84007/find-and-replace-text-within-multiple-files
#-----------------------------------------------------------------------------------
########################################################
dieukien=0
if [ $dieukien  == 1 ] ; then
	conda create -n P3 python=3.6 -y
	source activate P3
	    conda install tensorflow -y
	    conda install tensorflow-gpu -y
	    conda install keras-gpu=2.0 -y
	    conda install keras=2.0 -y # keras moi khong co ham 'merge'
	    pip install pydub -y
	    #pip install jieba # chinese split sentence to words
	    pip install pinyin # use in: https://github.com/hermanschaaf/mafan
	    pip install python-levenshtein
	    sudo apt-get install graphviz -y
	    pip install pydot
	    pip install librosa
	    conda install -c menpo ffmpeg
	    
	    #Install jupiter ipython highlight notebook:
	    #https://github.com/jcb91/jupyter_highlight_selected_word
	    #https://github.com/ipython-contrib/jupyter_contrib_nbextensions
	    conda install -c conda-forge jupyter_contrib_nbextensions -y
	    conda install -c conda-forge jupyter_highlight_selected_word -y #
	    jupyter nbextension enable highlight_selected_word/main
	    #conda install -c anaconda flask -y # minimal webservice for python: https://www.youtube.com/watch?v=_yoxrAIf5u4
	    pip install more_itertools # for list padding, https://stackoverflow.com/questions/3438756/some-built-in-to-pad-a-list-in-python
	source deactivate
fi
#samba:
# sudo system-config-samba
########################################################
########################################################
desktop = 1
if [ $desktop == 1 ] ; then
    #install package via GUI
    sudo dpkg –add-architecture i386
    sudo apt install wine64
    sudo apt-get install cups-pdf -y # print to PDF
fi
########################################################1
docker=1
if [ $docker == 1 ]; then #1
    # Install Docker-CE ubuntu:
    sudo apt-get update
    sudo apt-get install  -y   apt-transport-https     ca-certificates     curl     software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo apt-key fingerprint 0EBFCD88
    
    sudo apt-get update
    sudo apt-get install docker-ce
    sudo docker run hello-world
    
    # Install Nvidia-Docker:
    # If you have nvidia-docker 1.0 installed: we need to remove it and all existing GPU containers
    docker volume ls -q -f driver=nvidia-docker | xargs -r -I{} -n1 docker ps -q -a -f volume={} | xargs -r docker rm -f
    sudo apt-get purge -y nvidia-docker

    # Add the package repositories
    curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
      sudo apt-key add -
    distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
    curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
      sudo tee /etc/apt/sources.list.d/nvidia-docker.list
    sudo apt-get update

    # Install nvidia-docker2 and reload the Docker daemon configuration
    sudo apt-get install -y nvidia-docker2
    sudo pkill -SIGHUP dockerd

    # Test nvidia-smi with the latest official CUDA image
    docker run --runtime=nvidia --rm nvidia/cuda:9.0-base nvidia-smi
    
    # Ket qua: Hien thi duoc nvidia-smi la OK!
fi
########################################################

########################################################

########################################################2
Server=0
if [ $Server  == 1 ] ; then #1
    echo "ubuntu-desktop ..." & sudo apt-get install  -y --no-install-recommends ubuntu-desktop gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal
    echo "gnome-pane     ..." & sudo apt-get install  -y gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal
    echo "install ffmpeg ..." & sudo apt-get install  -y gnome-core xfce4 firefox nano -y --force-yes

    echo "Config login root user"
    sudo sed -i 's/prohibit-password/yes/' /etc/ssh/sshd_config
    sudo sed -i 's/#PermitRootLogin/PermitRootLogin/' /etc/ssh/sshd_config
fi  
########################################################
dieukien=0
if [ $dieukien  == 1 ] ; then
    #wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    #sudo gdebi google-chrome-stable_current_amd64.deb  -y
    sudo apt-get install redshift redshift-gtk  -y
    sudo apt install snapd   -y 
    #Install Shotcut Video Editor in Linux  
    sudo snap install shotcut --classic   -y
    # @@@ go and install: https://code.visualstudio.com/
    # @@@ Peek – A Simple Animated Gif Screen Recorder for Linux:
    sudo apt-get update   -y
    sudo apt-get install peek   -y

    # Install photo Editor:
    #install Pinta
    sudo apt-get install pinta
    #install GIMP
    # Uninstall GIMP:
    #sudo apt-get autoremove gimp gimp-plugin-registry
    sudo apt-get update
    sudo apt-get install gimp
    # Install OBS:
    sudo apt-get update
    sudo apt-get install obs-studio -y
    # install chroma-key-software-live-streaming green screen:
    # bai goc: https://streamshark.io/blog/chroma-key-software-live-streaming/
    # https://github.com/obsproject/obs-studio/wiki/Install-Instructions#linux

fi
########################################################
dieukien=0
if [ $dieukien  == 1 ] ; then
    # Install FreeCAD like autocad (269MB)
    #sudo apt install freecad -y  # khong load duoc webgui
    # hoac:
    sudo apt install librecad -y
fi
########################################################5
dieukien=0
if [ $dieukien  == 1 ] ; then
    echo "Install Anaconda: CD to Anaconda path" 
    bash Anaconda3-5.2.0-Linux-x86_64.sh 
    PATH=/home/u/anaconda3/bin:$PATH
    #~ sudo apt install nvidia-340      
    #~ sudo apt install nvidia-utils-390
    conda install -c anaconda anaconda-navigator -y
fi
########################################################
dieukien=0
if [ $dieukien  == 1 ] ; then
    #install Pytorch Windows-------------------------
    conda create -n pytorch_env python -y #~200MB
    source activate pytorch_env
    conda install -c soumith pytorch -y #590MB
    #python
    #import torch
fi    
########################################################

########################################################6
Server=0
if [ $Server  == 1 ] ; then
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
dieukien=0
if [ $dieukien  == 1 ] ; then
    # install youtube list downloader:
    sudo apt-get install wget   # https://smallbusiness.chron.com/use-wget-ubuntu-52172.html
    sudo apt install libqtwebkit4 -y
    sudo apt-get install youtube-dl -y # down tai cty k dc, mat mang ngay
fi

########################################################8
# END AUTO RUN
########################################################9


#Auto rename files: interminal
# j=1;for i in *.mp4; do mv "$i" file"$j".mp4; let j=j+1;done

##########
#cai tren win/ubuntu:
# De doi thu muc mac dinh cua jupyter notebook:
# open jupyter as normal, open new terminal, run: 
#    jupyter notebook --generate-config    # it will create a file, will show dir, open that file, 
# 
# Search for the following line: #c.NotebookApp.notebook_dir = ''
# Replace by c.NotebookApp.notebook_dir = 'f:/the/path/to/home/folder/of/jupyter'


# tham khao: https://www.linkedin.com/pulse/installing-nvidia-cuda-80-ubuntu-1604-linux-gpu-new-victor
