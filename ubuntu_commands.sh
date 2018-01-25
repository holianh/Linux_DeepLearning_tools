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














