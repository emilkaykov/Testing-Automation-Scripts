#!/bin/bash

# script to software updates automatically


apt list --upgradable
sudo apt-get update -yy

echo -e "Software Updates Installed\nHave a nice day!"

sleep 2


