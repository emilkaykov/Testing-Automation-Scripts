#!/bin/bash

find . -iname '*nov mix-*' 

for x in ./*; do mv "$x" "${x%nov mix-*.mp3}.mp3 ; done




