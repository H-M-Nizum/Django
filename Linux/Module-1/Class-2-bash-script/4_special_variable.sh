#!/bin/bash

# Print My Current Script
echo "My Current Script is : $0"

# Pass Argument When i run bash script EX: ./4_special_variable.sh 23
# Get First Agrument
echo "First Agrument : $1"

# Get Second Agrument
echo "Second Agrument : $2"

# Get All Agrument
echo "All Agrument : $@"

# Get Process id
echo "My Process Id: $$"