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
VD:
sshfs tact@192.168.0.6:/home/tact/AudioDBs/Olivia/logs ~/kr/logs
    ref:https://stackoverflow.com/questions/37987839/how-can-i-run-tensorboard-on-a-remote-server


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

sudo apt-get install geany






