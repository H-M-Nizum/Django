#!/bin/bash   
# This line tells the system to use the Bash shell to run the script

# Print a message to the user
echo "Enter Your Name : "

# Declare a variable and assign user input to it
# The 'read' command takes input from the user
# The input value will be stored in the variable "name"
read name

# Use the variable
# To access the value of a variable, use the $ symbol before the variable name
echo "My name is $name"
