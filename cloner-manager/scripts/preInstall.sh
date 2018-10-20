#!/bin/bash

USERNAME=cloner-manager

groupadd ${USERNAME}
useradd -Mg ${USERNAME} ${USERNAME}
