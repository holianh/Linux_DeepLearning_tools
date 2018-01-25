# Linux DeepLearning tools
These are some useful tools to use with Linux (focus on Ubuntu) when working with Deep Learning.

# Linux system:
Useful linux command
  - __htop__: to view in %CPU uses by threads, %RAM: kill thread, filter, search,...
  - __ncdu__: to view files/folders size over local or ssh
  - __find -type f -name "*libcudnn.so*"__ : find file/folder in Linux, [more](ubuntu_commands.sh#L14)
  - __rm -fdr <dir_name>__: Remove a dir with contents, [more](ubuntu_commands.sh#L2)
  - __sudo lshw -class disk -short__ : List Physical Hardisk in Ubuntu, [view](ubuntu_commands.sh#L21)
# Check Envs for Deep Learning:
  - nvidia-smi
  - nvcc -V
  - find -type f -name "*libcudnn.so*"
  - nvidia-smi --format=csv,noheader --query-gpu=index,name,temperature.gpu,fan.speed,pstate,power.draw,clocks.current.graphics, [more](ubuntu_commands.sh#L6)

  # Install Deeplearning Libraries:
  - pipreqs /path/to/project: PYTHON - AUTO GENERATE REQUIREMENTS.TXT, [more]((ubuntu_commands.sh#L33))
  - pip install python-levenshtein
  - 
  
  # Python functions List:
   - def LastNlines\(NLs=15,LineContainKey="Key to Fine"\), [view](python_funcs_codes.py#L7)
   -  Plot history and accuray when training with Keras to PDF, [view](python_funcs_codes.py#L38)
   - Save data to json file, [view](python_funcs_codes.py#L113) 
   - Files_2csv_inDir: Find and Add All wav & label files to *.CSV, [view](python_funcs_codes.py#L130)
   - Timing: Calculate running time, [view](python_funcs_codes.py#L174) 
   - Get date time, month, day, hour, minute,...[view](python_funcs_codes.py#L272)
   - Post (upload) file/string to PHP webpage, [view](python_funcs_codes.py#L195)
   - Run a system Ubuntu command, [view](python_funcs_codes.py#L223) 
   - Substring: Copy contends from txt file, add string of time, add ... [view](python_funcs_codes.py#L229)
   - []() 
   - []()
   - []() 
   - []()
   - []() 
   - []()
   - []() 
   - []()
   - []() 
   
   
   
   
   
   
   
   
   
   
   
