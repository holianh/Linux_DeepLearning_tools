#!/bin/bash

#tar_npy.sh

#tar & untar
#tham so:
# $3: duong dan thu muc chua *.npy
# $2: ten file tar.gz
# $1: =1: giai nen
#     =0: nen file

# Nen:
#  bash tar_npy.sh    1    ta.tar.gz      /home/ubu/ubuntu/ChineseADB/All_database_processed/home/ubuntu/ChineseADB/All_database_processed/Train_npy 

# Giai Nen:
#  bash tar_npy.sh    0    ta.tar.gz      /home/ubu/ubuntu/ChineseADB/All_database_processed/home/ubuntu/ChineseADB/All_database_processed/Train_npy 

cd $3
if (($1 > 0)) ; then 
    tar -czvf  $2  *.npy
    rm *.npy
else    
    tar -xvzf  $2
fi






