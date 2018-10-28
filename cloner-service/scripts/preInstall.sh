#!/bin/bash

USERNAME=cloner-service

getent group ${USERNAME} || groupadd ${USERNAME}
getent passwd ${USERNAME} || useradd -Mg ${USERNAME} ${USERNAME}
