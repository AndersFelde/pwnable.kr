#!/bin/bash
mkdir $1
scp -r -P 2222 $1@pwnable.kr:/home/$1 ./
