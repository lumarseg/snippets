#!/bin/bash

# Request the IAM Role Name
clear
echo "- Please, write a name of a EKS Cluster Role (up to 30 ASCII chars, ie: eksClusterRole)"
read -p "  EKS Cluster Role name: " eksClusterRole

# Check that the name is not empty
if [ -z "$eksClusterRole" ]; then
  echo "EKS Cluster Role name cannot be empty."
  exit 1
fi

# Verify that the name does not contain leading or trailing whitespace
if [[ ! "$eksClusterRole" =~ ^[a-zA-Z0-9_-]+$ ]]; then
  echo "EKS Cluster Role name cannot contain leading or trailing whitespace."
  exit 1
fi

# Check that the name is less than 30 characters
if [ ${#eksClusterRole} -gt 30 ]; then
  echo "EKS Cluster Role name must be less than 30 characters."
  exit 1
fi

# Run the AWS CLI command to create the IAM Role
echo
aws iam create-role --role-name $eksClusterRole --assume-role-policy-document file://trust-policy.json

# Associate the "AmazonEKSClusterPolicy" policy with the role.
aws iam attach-role-policy --role-name $eksClusterRole --policy-arn arn:aws:iam::aws:policy/AmazonEKSClusterPolicy

# Verify the policy.
aws iam list-attached-role-policies --role-name $eksClusterRole

# Run the AWS CLI command to get de ARN of the IAM Role
arn=$(aws iam get-role --role-name $eksClusterRole --query "Role.Arn" --output text)

echo
echo "The ARN number of $eksClusterRole is: $arn"
echo "$eksClusterRole | $arn" >> arn_list.tmp
echo
echo Done !!!
echo

