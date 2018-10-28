#!/bin/bash

USERNAME=cloner-manager

getent group ${USERNAME} || groupadd ${USERNAME}
getent passwd ${USERNAME} || useradd -Mg ${USERNAME} ${USERNAME}
