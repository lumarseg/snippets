#!/bin/bash

# Upload Template
aws s3 cp kubernetes-demo.yaml s3://lumarseg-cf-templates/kubernetes-demo/

# Create Stack
aws cloudformation create-stack \
  --stack-name kubernetes-demo \
  --template-url https://lumarseg-cf-templates.s3.amazonaws.com/kubernetes-demo/kubernetes-demo.yaml \
  --capabilities CAPABILITY_NAMED_IAM

echo
echo Done !!!
echo

