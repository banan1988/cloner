#!/bin/bash

USERNAME=cloner-service

groupadd ${USERNAME}
useradd -Mg ${USERNAME} ${USERNAME}
