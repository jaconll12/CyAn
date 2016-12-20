#!/bin/bash 
source config.sh

m=$(date +%B)
d=$(date +%d)
y=$(date +%Y)
folder=$d$m$y
folder1= $Environment/$folder
echo $folder1
cd archive
if [ -d $folder1 ]; then
    cp results/* $folder1
    echo "it exists"
fi
    
 if [ ! -d $folder1 ]; then
    mkdir $folder1/
    cp results/* $folder1
    echo "Needed to create it"
fi

rm results/*
