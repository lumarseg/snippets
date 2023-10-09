#!/bin/bash

# Request the name of the Keypair from the user
read -p " - Please, write a name of a new Keypair (up to 30 ASCII chars): " keypair_name

# Check that the name is not empty
if [ -z "$keypair_name" ]; then
  echo "The key pair name cannot be empty."
  exit 1
fi

# Verify that the name does not contain leading or trailing whitespace
if [[ ! "$keypair_name" =~ ^[a-zA-Z0-9_-]+$ ]]; then
  echo "The Keypair name cannot contain leading or trailing whitespace."
  exit 1
fi

# Check that the name is less than 30 characters
if [ ${#keypair_name} -gt 30 ]; then
  echo "The Keypair name must be less than 30 characters."
  exit 1
fi

# Run the AWS CLI command to create the Keypair
aws ec2 create-key-pair --key-name "$keypair_name" --key-type ed25519 --query 'KeyMaterial' --output text > "${keypair_name}.pem"

# Move Keypair to ""
mv "${keypair_name}.pem" ~/.ssh/"${keypair_name}.pem"
sudo chmod 600 ~/.ssh/"${keypair_name}.pem"

# Check if the command was executed correctly
if [ $? -eq 0 ]; then
  echo "The Keypair '$keypair_name' has been successfully created and saved to '${keypair_name}.pem'."
else
  echo "An error occurred while creating the Keypair."
fi
