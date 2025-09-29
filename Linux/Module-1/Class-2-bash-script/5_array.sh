#!/bin/bash

# Array Declartion
declare -a subjects=("Bangla" "English" "Math")

# Print First Indecx value
echo "First Index Value is : ${subjects[0]}"

# Print Second Indecx value
echo "Second Index Value is : ${subjects[1]}"


# Iterate Array Using Form Loop
for subject in "${subjects[@]}"; do
    echo "$subject"
done