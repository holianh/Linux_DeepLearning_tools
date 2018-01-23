# Linux DeepLearning tools
These are some useful tools to use with Linux (focus on Ubuntu) when working with Deep Learning.

# Linux system:
  - htop: to view in %CPU uses by threads, %RAM: kill thread, filter, search,...
  - ncdu: to view files/folders size over local or ssh
  - find file/folder in Linux:
    - find -name "\*ASR\*" : find all file/dir name include ASR
    - find -typy d -name "\*ASR\*" : find all *dir* name include ASR
    - find -type f -name "*libcudart*"   : find all files libcudart.so.* in current folder
    - find -type f -name "*libcudnn.so*"   : find all files libcudnn.so.*

# Check Envs for Deep Learning:
  - nvidia-smi
  - nvcc -V
  - find -type f -name "*libcudnn.so*"
  - nvidia-smi --format=csv --query-gpu=temperature.gpu,fan.speed,pstate,power.draw,clocks.current.graphics
  - nvidia-smi --format=csv,noheader --query-gpu=temperature.gpu,fan.speed,pstate,power.draw,clocks.current.graphics
  - nvidia-smi --format=csv --query-gpu=index,name,temperature.gpu,fan.speed,pstate,power.draw,clocks.current.graphics

  
  
  
