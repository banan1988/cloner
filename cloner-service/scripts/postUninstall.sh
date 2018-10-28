#!/bin/bash

USERNAME=cloner-service

# Cleanup
rm -rf /etc/cloner-service.d
rm -rf /opt/cloner-service
rm -rf /var/cloner-service
rm -rf /var/log/cloner-service

getent passwd ${USERNAME} && userdel ${USERNAME} || echo "User ${USERNAME} does not exist. Skip deleting..."
