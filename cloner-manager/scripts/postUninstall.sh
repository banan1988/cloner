#!/bin/bash

USERNAME=cloner-manager

# Cleanup
rm -rf /etc/cloner-manager.d
rm -rf /opt/cloner-manager
rm -rf /var/cloner-manager
rm -rf /var/log/cloner-manager

getent passwd ${USERNAME} && userdel ${USERNAME} || echo "User ${USERNAME} does not exist. Skip deleting..."
