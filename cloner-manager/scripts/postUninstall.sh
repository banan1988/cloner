#!/bin/bash

USERNAME=cloner-manager

# Cleanup
rm -rf /etc/cloner-manager.d
rm -rf /opt/cloner-manager
rm -rf /var/cloner-manager
rm -rf /var/log/cloner-manager

userdel ${USERNAME}
