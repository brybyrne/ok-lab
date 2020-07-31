#!/bin/bash

# Removes configuration files from configs directory as a clean up action

ECHO ""
ECHO "************ Listing files in /configs ************"
ECHO ""
ls -la ../configs

ECHO ""
ECHO "************ Removing cfg files from configs directory ************"
ECHO ""


rm -rf ../configs/*.cfg

ECHO ""
ECHO "************ Confirming Success (No Files Should Be Listed) ************"
ECHO ""

ls -la ../configs

ECHO ""
ECHO "************ END ************"
ECHO ""
