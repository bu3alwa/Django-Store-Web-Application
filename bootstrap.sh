#!/usr/bin/env bash

apt-get update
apt-get install -y python
apt-get install -y python-dev
apt-get install -y python-pip
apt-get install -y libmysqlclient-dev
apt-get install -y nginx

export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"
echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
apt-get update 
apt-get install -y google-cloud-sdk
apt-get install -y google-cloud-sdk-app-engine-python
apt-get install -y mysql-client

apt-get -y install mysql-server
