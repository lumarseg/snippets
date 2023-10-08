#!/bin/bash

sudo rm ~/.kube -rf
sudo snap install microk8s --classic
sudo mkdir ~/.kube
sudo usermod -a -G microk8s $USER
sudo chown -R $USER ~/.kube
newgrp microk8s
echo "alias k='microk8s kubectl'" >> ~/.bashrc
echo
echo done !!!
echo