sudo chown -R $USER /usr/local/bin
sudo mkdir /usr/local/lib/node_modules
sudo chown -R $USER /usr/local/lib/node_modules
#ensure current user has sudo access on this machine. If not, edit /etc/sudoers file.
sudo npm install -g strongloop
#Run same command again if you notice the above command runs for a while and in between you see any errors in the above command
sudo npm install -g strongloop

