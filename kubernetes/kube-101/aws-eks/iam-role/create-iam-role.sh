#!/bin/bash

# Request the IAM Role Name
clear
echo "- Please, write a name of a new IAM Role (up to 30 ASCII chars, ie: MyEKSRole)"
read -p "  IAM Role name: " iam_role_name

# Check that the name is not empty
if [ -z "$iam_role_name" ]; then
  echo "The IAM Role name cannot be empty."
  exit 1
fi

# Verify that the name does not contain leading or trailing whitespace
if [[ ! "$iam_role_name" =~ ^[a-zA-Z0-9_-]+$ ]]; then
  echo "The IAM Role name cannot contain leading or trailing whitespace."
  exit 1
fi

# Check that the name is less than 30 characters
if [ ${#iam_role_name} -gt 30 ]; then
  echo "The IAM Role name must be less than 30 characters."
  exit 1
fi

# Run the AWS CLI command to create the IAM Role
echo
aws iam create-role --role-name $iam_role_name --assume-role-policy-document file://trust-policy.json

# Run the AWS CLI command to get de ARN of the IAM Role
arn=$(aws iam get-role --role-name $iam_role_name --query "Role.Arn" --output text)

echo
echo "The ARN number of $iam_role_name is: $arn"
echo "$iam_role_name | $arn" >> arn_list.tmp
echo
echo Done !!!
echo

