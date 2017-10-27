#!/bin/bash

sudo cp -r hook_generator /opt
sudo chmod +x /opt/hook_generator/hook.sh 
sudo ln /opt/hook_generator/hook.sh /usr/bin/hook
