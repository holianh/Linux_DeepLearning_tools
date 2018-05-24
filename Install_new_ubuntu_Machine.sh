
########################################################
echo "Install APP"
sudo apt-get install openssh-server
sudo apt-get install htop
sudo apt-get install ncdu
sudo apt-get install geany -y
sudo apt-get install geany-plugins -y
sudo apt-get install tmux -y

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











































    