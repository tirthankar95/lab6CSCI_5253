#! /bin/bash
mkdir -p /home/timi5773/Desktop
cd /home/timi5773/Desktop
sudo add-apt-repository --yes universe
sudo apt --yes update
sudo apt install --yes python3-pip
pip3 install Flask
pip3 install jsonpickle
pip3 install pillow
pip3 install numpy
pip3 install grpcio-tools
git clone https://github.com/tirthankar95/lab6CSCI_5253.git