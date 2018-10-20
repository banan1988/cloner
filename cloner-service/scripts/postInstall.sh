#!/bin/bash

VIRTUAL_ENV_DIR=/var/cloner-service/virtualenv

# Create virtualenv
if [ -d "${VIRTUAL_ENV_DIR}" ] ; then
    echo "Directory ${VIRTUAL_ENV_DIR} exists."
else
    /usr/bin/virtualenv ${VIRTUAL_ENV_DIR}
fi

# Activate virtualenv
source /var/cloner-service/virtualenv/bin/activate

# Install packages
pip install PyYAML==3.13
pip install Flask==1.0.2
pip install requests==2.20.0
#pip install GitPython==2.1.11

# Deactivate virtualenv
deactivate

# Enable Gor for non-root users in a secure method
GOREPLAY=/opt/cloner-service/goreplay
setcap "cap_net_raw,cap_net_admin+eip" ${GOREPLAY}

# Reload systemd
/usr/bin/systemctl daemon-reload