# Menu
This is all Header in this file:
1. Linux DeepLearning tools, [view](#1-linux-deeplearning-tools)
2. Linux system, [view](#2-linux-system)
3. Check Envs for Deep Learning, [view](#check-envs-for-deep-learning)
4. Install Deeplearning Libraries, [view](#4-install-deeplearning-libraries)
5. Python functions List, [view](#5-python-functions-list)
6. Keras funcs list, [view](#6-keras-funcs-list)

# Link hay cần làm

[Link hay cần làm](Link-hay-can-lam.md)

# 1. Linux DeepLearning tools
These are some useful tools to use with Linux (focus on Ubuntu) when working with Deep Learning. [Tham khảo:](https://peshmerge.io/how-to-install-cuda-9-0-on-with-cudnn-7-1-4-on-ubuntu-18-04/)
  - 1. Install Ubuntu 18.04
    2. Install Nvidia-Driver: nvidia-smi
    3. Install cuda 9.0     : nvcc -V
    4. Install cudnn        
    5. Install Anaconda
    
  - Chạy trong Notebook, lấy thông tin của main, cpu, [more](ubuntu_commands.sh#L369)

# 2. Linux system
Useful linux command
  - __htop__: to view in %CPU uses by threads, %RAM: kill thread, filter, search,...
  - __ncdu__: to view files/folders size over local or ssh
  - __find -type f -name "*libcudnn.so*"__ : find file/folder in Linux, [more](ubuntu_commands.sh#L14)
  - __rm -fdr <dir_name>__: Remove a dir with contents, [more](ubuntu_commands.sh#L2)
  - __sudo lshw -class disk -short__ : List Physical Hardisk in Ubuntu, [view](ubuntu_commands.sh#L21)
  - __Login to jupyter server from local machine__ , [view](ubuntu_commands.sh#L55)
  - __Linux system: share folder / mount a remote dir to local__ , [view](ubuntu_commands.sh#L98)
  - __Startup a program in ubuntu manualy__ , [view](ubuntu_commands.sh#L107)
  - Linux system: install code editor __geany__, better than gedit: code folding, show indent guide, show space,...  , [view](ubuntu_commands.sh#L142)
  - Ubuntu: Install Sublime Text in linux: [view](ubuntu_commands.sh#L287)
  - Ubuntu: Create bootable install OS disk (ubuntu/window/...system): [view](ubuntu_commands.sh#L257)
  - Install VNCserver in ubuntu: [good link](https://ubuntuwiki.com/2017/07/how-to-install-vnc-on-ubuntu-17-04/)
  - Install Samba and Share file from linux to windows [Xem](ubuntu_commands.sh#L298)
  - Run Specific CUDA on GPU: __CUDA_VISIBLE_DEVICES=2,3 python code.py__ or *export CUDA_VISIBLE_DEVICES=0,1*
  - Add New sudo User ubuntu (add user): [Xem](ubuntu_commands.sh#L384)
  - Change language in ssh of ubuntu to english: [Xem](ubuntu_commands.sh#L393)
  - TensorBoard server client:(server): tensorboard --logdir=. --host=0.0.0.0 --port=6006 ;(Local): http://ip:6006 [Xem](ubuntu_commands.sh#L406)
  - Install Vivaldi, import/export pass: [xem](Ubuntu_System.md#install-vivaldi)
  - Install flash player ubuntu success \[mothod1\]: (view here)[https://www.wikihow.com/Install-Flash-Player-on-Ubuntu]
  - FFMPEG Chia clip ra thành nhiều phần bằng nhau: [Xem](ubuntu_commands.sh#L432-L437)
  - Ubuntu nén, giải nén, compress tar, zip folder: [Xem](ubuntu_commands.sh#L441)
  - Ubuntu/windows tìm tên thiết bị camera/webcam: [/sbin/udevadm info --export-db | grep video](ubuntu_commands.sh#L452-L527)
  - ubuntu remove readonly files/folders permissions [sudo chmod 777 -R *](ubuntu_commands.sh#L527-L530)
  - Tạo phím tắt/shortcut cho "Open terminal here" [xem](Ubuntu_System.md#t%E1%BA%A1o-ph%C3%ADm-t%E1%BA%AFt-cho-open-terminal-here)
  - Ubuntu compress, zip, unzip files with progress: [xem](Ubuntu_System.md#ubuntu-compress-zip-unzip-files-with-progress)
  - Copy file in Ubuntu with progress:   [xem](Ubuntu_System.md#copy-file-in-ubuntu-with-progress)
  - folder size: !du -hs "dir/path/"
# 3. Check Envs for Deep Learning
  - nvidia-smi , watch -n 0.3 nvidia-smi, nvidia-smi -l 1
  - nvcc -V
  - find -type f -name "*libcudnn.so*"
  - nvidia-smi --format=csv,noheader --query-gpu=index,name,temperature.gpu,fan.speed,pstate,power.draw,clocks.current.graphics, [more](ubuntu_commands.sh#L6)
  - Anaconda GUI in ubuntu: *anaconda-navigator* [view more](ubuntu_commands.sh#L43)
  - Ubuntu: Run ipython notebook with browser from on server: *ipython notebook --no-browser --ip=0.0.0.0 --port=8889* :[more](ubuntu_commands.sh#L203)
  - ipython: ipython notebook width 100%   , [more](ubuntu_commands.sh#L224)
  - Anaconda ipython Jupyter Notebook: Change startup folder of notebook: [view](ubuntu_commands.sh#L332)
  - Anaconda Jupyter Notebook: Run Remote Notebook on server from local: [view](ubuntu_commands.sh#L351)
  
  # 4. Install Deeplearning Libraries
  - **Install all librarys** needing for Deeplearning with Keras for Speech: , [View](Install_python_libs.py#L1)
  - PYTHON - AUTO GENERATE REQUIREMENTS.TXT: __pipreqs .__  (pipreqs /path/to/project): [more](ubuntu_commands.sh#L33)
  - pip install python-levenshtein
  - How to install pytorch in Anaconda with conda or pip?  [View](ubuntu_commands.sh#L319)
  
  # 5. Python functions List
   - def LastNlines\(NLs=15,LineContainKey="Key to Fine"\), [view](python_funcs_codes.py#L7)
   -  Plot history and accuray when training with Keras to PDF, [view](python_funcs_codes.py#L38)
   - Save data to json file, [view](python_funcs_codes.py#L113) 
   - Files_2csv_inDir: Find and Add All wav & label files to *.CSV, [view](python_funcs_codes.py#L130)
   - New calculate Running time + progress display: [xem](taLibs_Datetime.md#class-running-time-waiting-time)
   - New calculate running time simple (rất đơn giản): [xem](taLibs_Datetime.md#running-time-waiting-time)
   - Datetime Vietnam timezone+7: [xem](taLibs_Datetime.md#date-time-7-vietnam-time)
   - Timing: Calculate running time, [view](python_funcs_codes.py#L174) 
   - Get date time, month, day, hour, minute,...[view](python_funcs_codes.py#L272)
   - Python: Many date time, unique file names: [view](python_funcs_codes.py#L421) 
   - Substring: Copy contends from txt file, add string of time, add ... [view](python_funcs_codes.py#L229)
   - [Get time of file to make filename](python_fn.md#get-time-of-file-to-make-filename)
   - Post (upload) file/string to PHP webpage, [view](python_funcs_codes.py#L195)
   - Run a system Ubuntu command, [view](python_funcs_codes.py#L223) 
   - Move, Copy, delete file from Python, [view](python_funcs_codes.py#L281) 
   - Delay, sleep in python, [view](python_funcs_codes.py#L298)
   - Pass arguments to program, call commandline args, [view](python_funcs_codes.py#L304)
   - Load json with multiple json lines, [view](python_funcs_codes.py#L327)
   - Python: Print json file out to screen:  [view](python_funcs_codes.py#L406)
   - Python: Padding a vector/matrix enlarge/make bigger  [view](python_funcs_codes.py#L468) 
   - Python: Run ubuntu command without display with subprocess.Popen, [view](python_funcs_codes.py#L481) 
   - Python: Compress folders at current folder to tar.gz   [view](python_funcs_codes.py#L497) 
   - Padding list 2D:  [view](python_funcs_codes.py#L515) 
   - Convert list of 2D array to 3D array [view](python_funcs_codes.py#L555 ) 
   - Python: paralell CPUs, tính toán song song: pool.map_async()... [view](python_funcs_codes.py#L565 ) 
   - Python Notebook parallel CPUs:[view](python_funcs_codes.py#L650 ) 
   - Github markdown: auto make table of content: [view](python_funcs_codes.py#L615 ) 
   - Python Notebook run sudo command: [view](python_funcs_codes.py#L666 ) 
   - Python: install Pythable, [view](ubuntu_commands.sh#L414-L432)
   - python Ramdom shuffle/choice list: random.shuffle(x)  [view](Keras_funcs.py#L532-L570)
   - Python Read image to list of array then Padding [View](python_funcs_codes.py#L686-L717)
   - Convert video+DarkLabel to YoLo label [View](DarkLabel_ConvertTools.py#L112)
   - import a file:
```python
!wget -O taLibs_imports.py  https://github.com/holianh/Linux_DeepLearning_tools/raw/master/taLibs_imports.py
clear_output()
exec(open('taLibs_imports.py').read())
``` 

   # 6. Keras funcs list
   this is all useful Keras functions, can be directly use
   - Keras: __save model + weight__ to files, [here](Keras_funcs.py#L2)
   - Keras: __load model + weight__ from files to numpy array, [here](Keras_funcs.py#L17)
   - __Tensorboard__: local and remote , [here](Keras_funcs.py#L42)
   - __Make model run in Multiple GPUs__, [From define input](python_funcs_codes.py#L347), [to parallel model in multiple GPUs](python_funcs_codes.py#L391)
   - Keras: parallel GPUs Model training V2:  [here](Keras_funcs.py#L61)
   - Plot, display model in jupyter notebook: [here](Keras_funcs.py#L462)  
   - tensorboard <enter>: locate tensorboard/program.py | xargs sed -i -e "s/logdir', ''/logdir', os.getcwd()/g"
   - Keras python jupyter notebook: Live plot Loss accuracy when training : [here](Keras_funcs.py#L475)
   - Keras check GPU exists: from tensorflow.python.client import device_lib;print(device_lib.list_local_devices())        
  # 7. WEB Services
  - Build a front end web application: Send data without reload page [Youtube](https://goo.gl/4jNWzF)
  - Edit ipython Notebook html scroll field: div class="..." => div class="..." style="overflow-y: scroll; height:400px;"
   
   
   # 7. Ứng dụng khác
   - Get link Fshare full speed:  [http://fullcrack.vn/get-link-fshare/](http://fullcrack.vn/get-link-fshare/) và [https://tools.nhacm.com/](https://tools.nhacm.com/)
