#!/bin/bash

# Variable Assign (no spaces around =)
first_name="H.M."
last_name="Nizum"

# String Concatenation
full_name="$first_name $last_name"

# Print Full Name
echo "My Full Name is $full_name."

# Get String length
echo "My Full Name Length is : ${#full_name}."

# String Slicing
echo "First Four Character From my Full Name : ${full_name:0:4}"

# Take Input From user and Assign this input in a variable
echo "Enter Your Age : "
read age
echo "I am $age year old."