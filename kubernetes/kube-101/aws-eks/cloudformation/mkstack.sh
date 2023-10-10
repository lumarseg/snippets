#!/bin/bash

# Upload Template
aws s3 cp eksClusterDemo.yaml s3://lumarseg-cf-templates/kubernetes-demo/

# Create Stack
aws cloudformation create-stack \
  --stack-name eksClusterDemo \
  --template-url https://lumarseg-cf-templates.s3.amazonaws.com/kubernetes-demo/eksClusterDemo.yaml \
  --capabilities CAPABILITY_NAMED_IAM

echo
echo Done !!!
echo

